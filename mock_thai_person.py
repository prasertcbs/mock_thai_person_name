# %% [markdown]
# # mock Thai person name
# * pythainlp: https://github.com/PyThaiNLP/pythainlp
#     * installation:
#         * `pip install pythainlp`
# %% [markdown]
# ---
# * author:  [Prasert Kanawattanachai](prasert.k@chula.ac.th)
# * YouTube: https://www.youtube.com/prasertcbs
# * [Chulalongkorn Business School](https://www.cbs.chula.ac.th/en/)
# ---

# %%
import pythainlp.corpus as pc
import random
import pandas as pd

# %%
class Mock_thai_name():
    female_names=list(pc.thai_female_names())
    male_names=list(pc.thai_male_names())
    family_names=list(pc.thai_family_names())
    
    def __init__(self, female_n:int=1, male_n:int=1, output_csv_filename=None):
        """สุ่มชื่อภาษาไทยโดยระบุจำนวนชื่อผู้หญิงและผู้ชาย

        Args:
            female_n (int, optional): จำนวนชื่อผู้หญิง. Defaults to 1.
            male_n (int, optional): จำนวนชื่อผู้ชาย. Defaults to 1.
            output_csv_filename ([type], optional): save ผลลัพธ์เป็น csv file. Defaults to None.
        """        
        females=random.sample(self.female_names, female_n)
        females_family=random.sample(self.family_names, female_n)
        males=random.sample(self.male_names, male_n)
        males_family=random.sample(self.family_names, male_n)
        dict_female={'fname': females, 'lname': females_family, 'gender': 'f'}
        dict_male={'fname': males, 'lname': males_family, 'gender': 'm'}
        self.df=pd.concat([pd.DataFrame(dict_female), pd.DataFrame(dict_male)])
        if output_csv_filename:
            self.df.to_csv(output_csv_filename, index=False)
        

# %%
if __name__ == "__main__":
    m=Mock_thai_name()
    print(m.df)
    m2=Mock_thai_name(3, 2)
    print(m2.df)
    m3=Mock_thai_name(3, 2, 'mock_thai_person.csv')
    print(m3.df)

# %%
