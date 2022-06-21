'''
For Django Shell only
'''

import threading
import json
from pathlib import Path
from typing import List
from decimal import Decimal
import numpy as np
import pandas as pd
from pandas import read_excel, read_csv, DataFrame
from option.models import (
    WenOptionCategory,
    WangOptionCategory,
    WenOption,
    WangOption,
    PulseOption,
    DiseaseOptionCategory,
    DiseaseOption,
    EyeCategory,
    EyeOption,
    TongueCategory,
    TongueOption,)
from acupuncture.models import (
    Acupuncture, 
    DongAcupuncture, 
    AcupunctureArea, 
    DongAcupunctureArea)
from medicines.models import (
    Medicine, 
    InjuryTreatment, 
    Decoction, 
    DecoctionComponents)
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
    

    def __init__(self) -> None:
        self.med_path =  Path(r'./extern/medicines/medicine.csv')


    def put_it(self,):
        df = read_csv(self.med_path)
        df.fillna('', inplace=True)
        rows = [Medicine(
                type=row['MedicineType'],
                name=row['MedicineName'], 
                bopomofo=row['MedicineBopomoCode'], 
                nhi_id=row['MedicineNHIID'],
                nhi_name=row['MedicineNHIName'],
                manufacturer=row['MedicineManufacturer'],
                # cost=Decimal(row['MedicineCost']),
                # price=Decimal(row['MedicinePrice']),
                info=row['MedicineInfo'],
                unit=row['MedicineUnit'],
            ) 
            for _, row in df.iterrows()]
        Medicine.objects.bulk_create(rows)


class ExternOption:
    
    def __init__(self):
        self.disease_cat = Path(r'./extern/options/diseaseCategory.csv')
        self.disease_option = Path(r'./extern/options/diseaseOption.csv')
        self.pulse_option = Path(r'./extern/options/pulseOption.csv')
        self.wen_cat = Path(r'./extern/options/wenCategory.csv')
        self.wang_cat = Path(r'./extern/options/wangOptionCategory.csv')
        self.wen_option = Path(r'./extern/options/wenOption.csv')
        self.wang_option = Path(r'./extern/options/wangOption.csv')

        # ----------------------------------------------------------------

        self.eye_option = Path(r'./extern/options/eyeOption.csv')
        self.eye_cat = Path(r'./extern/options/eyeCategory.csv')
        self.tongue_option = Path(r'./extern/options/tongueOption.csv')
        self.tongue_cat = Path(r'./extern/options/tongueCategory.csv')
    
    
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
    

    def put_tongue_and_eye(self):
        df = read_csv(self.eye_cat)
        rows = [EyeCategory(name=row['CategoryName']) for _, row in df.iterrows()]
        EyeCategory.objects.bulk_create(rows)
        
        df = read_csv(self.eye_option)
        rows = [EyeOption(category=EyeCategory.objects.get(pk=row['CategoryFK']), option=row['OptionName']) for _, row in df.iterrows()]
        EyeOption.objects.bulk_create(rows)

        df = read_csv(self.tongue_cat)
        rows = [TongueCategory(name=row['CategoryName']) for _, row in df.iterrows()]
        TongueCategory.objects.bulk_create(rows)

        df = read_csv(self.tongue_option)
        rows = [TongueOption(category=TongueCategory.objects.get(pk=row['CategoryFK']), option=row['OptionName']) for _, row in df.iterrows()]
        TongueOption.objects.bulk_create(rows)


class ExternAcc:

    def __init__(self,):
        self.acu = Path(r'./extern/acupuncture/accu.csv')
        self.acu_area = Path(r'./extern/acupuncture/accuArea.csv')
        self.dong_acu = Path(r'./extern/acupuncture/dongAccu.csv')
        self.dong_acu_area = Path(r'./extern/acupuncture/dongAccuArea.csv')
    

    def put_it(self):
        
        df = read_csv(self.acu_area)
        rows = [AcupunctureArea(part=row['part']) for _, row in df.iterrows()]
        AcupunctureArea.objects.bulk_create(rows)

        df = read_csv(self.dong_acu_area)
        rows = [DongAcupunctureArea(part=row['part']) for _, row in df.iterrows()]
        DongAcupunctureArea.objects.bulk_create(rows)

        df = read_csv(self.acu)
        df = df.fillna('')
        rows = [
            Acupuncture(
                name=row['name'], 
                part=AcupunctureArea.objects.get(pk=row['part']), 
                alias=row['alias'], 
                link=row['link']) 
                for _, row in df.iterrows()]
        Acupuncture.objects.bulk_create(rows)

        df = read_csv(self.dong_acu)
        df = df.fillna('')
        rows = [
            DongAcupuncture(
                name=row['name'], 
                part=DongAcupunctureArea.objects.get(pk=row['part']), 
                link=row['link']) 
                for _, row in df.iterrows()]
        DongAcupuncture.objects.bulk_create(rows)


class ExternInjury:
    
    def __init__(self) -> None:
        self.injury = Path('./extern/injury/InjuryTreatment.csv')

    
    def put_it(self) -> None:
        df = read_csv(self.injury)
        df.fillna('', inplace=True)
        rows = [
            InjuryTreatment(
                name=row['InjuryTreatmentName'], 
                unit=row['InjuryTreatmentUnit'], 
                code=row['InjuryTreatmentNHICode']) 
                for _, row in df.iterrows()]
        InjuryTreatment.objects.bulk_create(rows)


class ExternDecoction:
    
    def __init__(self) -> None:
        self.decoction = Path('./extern/decoction/decoction.csv')
        self.decoction_comp = Path('./extern/decoction/decoctionCompo.csv')
    
    def put_it(self) -> None:
        df = read_csv(self.decoction)
        df.fillna('', inplace=True)
        
        rows = [
            Decoction(
                name=row['DecoctionName'], 
                bopomofo=row['DecoctionBopomoCode'], 
                # cost=Decimal(row['DecoctionCost']), 
                # price=Decimal(row['DecoctionPrice']),
                info=row['DecoctionInfo']) 
                for _, row in df.iterrows()]
        Decoction.objects.bulk_create(rows)
    
        df = read_csv(self.decoction_comp)
        df.fillna('', inplace=True)
        
        rows = [
            DecoctionComponents(
                decoction_id=Decoction.objects.get(pk=row['DecoctionID']), 
                medicine_id=Medicine.objects.get(pk=row['MedicineID']), 
                dosage=Decimal(row['CompoDosage']),
                unit=row['CompoUnit']) 
                for _, row in df.iterrows()]
        DecoctionComponents.objects.bulk_create(rows)



def main() -> None:
    '''
    python manage.py shell
    >>> exec(open('extern.py').read())
    '''
    print('[Running]')
    ExternMedicines().put_it()
    ExternInjury().put_it()
    ExternDecoction().put_it() 
    # ExternAcc().put_it()
    print('[Done]')
    # ExternOption().put_tongue_and_eye()
    # ExternDiseases().diseases_csv_to_db()
    # ExternMedicines('fang').json_to_db()
    # ExternMedicines('yao').json_to_db()
    # ExternMedicines('fang').db_change_all_med_titles()

main()