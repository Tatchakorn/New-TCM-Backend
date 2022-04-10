'''
For Django Shell only
'''

import threading
import json
from pathlib import Path
from typing import List
from pandas import read_excel, read_csv, DataFrame
from option.models import (
    WenOptionCategory,
    WangOptionCategory,
    WenOption,
    WangOption,
    PulseOption,
    DiseaseOptionCategory,
    DiseaseOption,)
from django.contrib.auth.models import User
# from diseases.models import Diseases
# from patients.models import PatientsInfo
# from medicines.models import FangMedicines, YaoMedicines


class ExternDiseases:

    def __init__(self) -> None:
        self.exel_file = Path(r'./extern/26082_1_1.6.1中文版ICD-10-CM更新第3版.xls')

    
    def get_sheets(self) -> List[str]:
        sheets = read_excel(self.exel_file, sheet_name=None)
        # Get all sheets
        return list(sheets.keys())
    

    def diseases_to_csv(self, sheet: str, i: int) -> None:
        df_dict = {}
        df_dict_index = 0
        df = read_excel(self.exel_file, sheet_name=sheet, header=1)
        df.set_axis(['code', 'string'], axis=1, inplace=True)
        df_en = df.loc[~df['code'].isnull(),:].iterrows()
        df_ch = df.loc[df['code'].isnull(),:].iterrows()
        for (_, en), (_, ch) in zip(df_en, df_ch):
            df_dict[df_dict_index] = {
                'code': en.code.strip(), 
                'en_name': en.string.strip(), 
                'ch_name': ch.string.strip(),
                }
            df_dict_index += 1

        df = DataFrame.from_dict(df_dict, 'index')
        df.to_csv(f'./extern/diseases/d_{i}.csv')


    def run(self) -> None:
        threads = []
        for i, sheet in enumerate(self.get_sheets()):
            t = threading.Thread(target=self.diseases_to_csv, args=(sheet, i,))
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()


    @staticmethod
    def diseases_csv_to_db() -> None:
        disease_csv_files = Path(r'./extern/diseases/').glob('*.csv')
        for file in disease_csv_files:
            df = read_csv(file)

            rows = [Diseases(code=row.code, en_name=row.en_name, ch_name=row.ch_name) 
                for _, row in df.iterrows()]
            Diseases.objects.bulk_create(rows)


class ExternMedicines:
    
    def __init__(self, option: str) -> None:
        '''
        option: "fang" or "yao"
        '''
        fang_path = Path(r'./extern/medicines/fang/fang_data.json')
        yao_path =  Path(r'./extern/medicines/yao/yao_data.json')
        self.json_file = fang_path if option == 'fang' else yao_path
        self.db_obj = FangMedicines if option == 'fang' else YaoMedicines
    
    @staticmethod
    def read_json(path: Path) -> dict:
        with open(path, 'r', encoding='utf-8') as f:
            j = dict(json.loads(f.read()))
        return j
    
    def json_to_db(self) -> None:
        data = self.read_json(self.json_file)
        rows = [self.db_obj(bapomofo=key,name=_key,info=_val) 
                for key, val in data.items()
                for _key, _val in val.items()]
        self.db_obj.objects.bulk_create(rows)
    
    def db_delete_all(self):
        self.db_obj.objects.all().delete()
    
    def db_change_all_med_titles(self):
        # print(type(self.db_obj.objects.all()))
        for i in self.db_obj.objects.all():
            print(type(i))
            print(str(i))
        # for i in self.db_obj.objects.all():
        #     print(i)



class ExternOption:
    
    def __init__(self):
        self.disease_cat = Path(r'./extern/options/diseaseCategory.csv')
        self.disease_option = Path(r'./extern/options/diseaseOption.csv')
        self.pulse_option = Path(r'./extern/options/pulseOption.csv')
        self.wen_cat = Path(r'./extern/options/wenCategory.csv')
        self.wang_cat = Path(r'./extern/options/wangOptionCategory.csv')
        self.wen_option = Path(r'./extern/options/wenOption.csv')
        self.wang_option = Path(r'./extern/options/wangOption.csv')

    
    def option_csv_to_db(self, csv_path: Path, db_object):
        df = read_csv(csv_path)
        rows = [row for _, row in df.iterrows()]

    
    def put_all_to_db(self):
        df = read_csv(self.disease_cat)
        rows = [DiseaseOptionCategory(name=row['name']) for _, row in df.iterrows()]
        DiseaseOptionCategory.objects.bulk_create(rows)

        
        df = read_csv(self.disease_option)
        rows = [DiseaseOption(option=row['option'], category=DiseaseOptionCategory.objects.get(pk=row['category'])) for _, row in df.iterrows()]
        DiseaseOption.objects.bulk_create(rows)
        
        df = read_csv(self.pulse_option)
        rows = [PulseOption(option=row['option']) for _, row in df.iterrows()]
        PulseOption.objects.bulk_create(rows)

        df = read_csv(self.wen_cat)
        rows = [WenOptionCategory(name=row['name']) for _, row in df.iterrows()]
        WenOptionCategory.objects.bulk_create(rows)

        df = read_csv(self.wang_cat)
        rows = [WangOptionCategory(name=row['name']) for _, row in df.iterrows()]
        WangOptionCategory.objects.bulk_create(rows)
        
        df = read_csv(self.wen_option)
        rows = [WenOption(option=row['option'], category=WenOptionCategory.objects.get(pk=row['category']))  for _, row in df.iterrows()]
        WenOption.objects.bulk_create(rows)
        
        df = read_csv(self.wang_option)
        rows = [WangOption(option=row['option'], category=WangOptionCategory.objects.get(pk=row['category'])) for _, row in df.iterrows()]
        WangOption.objects.bulk_create(rows)




def main() -> None:
    '''
    python manage.py shell
    >>> exec(open('extern.py').read())
    '''
    print('[Running]')
    ExternOption().put_all_to_db()
    print('[Done]')
    # ExternDiseases().diseases_csv_to_db()
    # ExternMedicines('fang').json_to_db()
    # ExternMedicines('yao').json_to_db()
    # ExternMedicines('fang').db_change_all_med_titles()

main()

if __name__ == '__main__':
    main()