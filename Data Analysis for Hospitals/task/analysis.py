# Data Analysis For Hospitals (Python / Introduction To Data Science)
# https://github.com/imprvhub/data-analysis-for-hospitals-jbrains
# Graduate Project Completed By Iván Luna, August 24, 2023.
# For Hyperskill (Jet Brains Academy). Course: Introduction To Data Science.

import glob
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


class AnalysisHospitals:
    column_data = [
        'bmi', 'diagnosis', 'blood_test', 'ecg',
        'ultrasound', 'mri', 'xray', 'children', 'months'
    ]d

    def __init__(self):
        pass

    @staticmethod
    def data_all_csv():
        dataframes_list = [v for v in map(pd.read_csv, glob.glob('test/*.csv'))]
        dataframes_list[1].rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
        dataframes_list[2].rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

        df = pd.concat(dataframes_list, ignore_index=True)
        df.drop(columns=['Unnamed: 0'], inplace=True)
        df.dropna(how='all', inplace=True)

        df['gender'] = df['gender'].replace(['male', 'man'], 'm')
        df['gender'] = df['gender'].replace(['female', 'woman', np.nan], 'f')

        for i in AnalysisHospitals.column_data:
            df[i].fillna(0, inplace=True)

        q1 = df['hospital']
        q1_answer = q1.value_counts().keys()[0]

        q2 = df[q1 == 'general']
        q2_answer = len(q2.query('diagnosis == "stomach"')) / len(q2)

        q3 = df.query('hospital == "sports"')
        q3_answer = len(q3.loc[q3['diagnosis'] == 'dislocation']) / len(q3)

        q4_answer = df.query('hospital == "general"').age.median() - df[df['hospital'] == 'sports']['age'].median()

        df.plot(y='age', kind='hist', bins=80)
        plt.show()
        print('The answer to the 1st question: 15-35')

        df['diagnosis'].value_counts().plot(kind='pie')
        plt.show()
        print('The answer to the 2nd question: pregnancy')

        df['age'].value_counts().plot(kind='box')
        plt.show()
        print('The answer to the 3nd question: It\'s because fucking stage')


def main():
    AnalysisHospitals.data_all_csv()


if __name__ == '__main__':
    main()