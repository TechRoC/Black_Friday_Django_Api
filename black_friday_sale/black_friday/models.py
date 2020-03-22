from django.db import models

# Create your models here.
class price(models.Model):
    PRODUCT_CHOICE = (
        ('P0069042','P00069042'),
        ('P00248942','P00248942'),
        ('P00087842','P00087842'),
        ('P00085442','P00085442')
    )
    GEN_CHOICE = (
        ('M','M'),
        ('F','F')
    )
    AG_CHOICE = (
        ('0-17','0-17'),
        ('18-25','18-25'),
        ('26-35','26-35'),
        ('36-45','36-45'),
        ('46-50','46-50'),
        ('51-55','51-55'),
        ('55+','55+')
    )
    CIT_CAT = (
        ('A','A'),
        ('B','B'),
        ('C','C')
    )
    STAY = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4+','4+')
    )
    User_ID =models.IntegerField(default=0)
    Product_ID= models.CharField(max_length=15, choices=PRODUCT_CHOICE)
    Gender= models.CharField(max_length=15, choices=GEN_CHOICE)
    Age= models.CharField(max_length=15, choices=AG_CHOICE)
    Occupation = models.IntegerField(default=0)
    City_Category = models.CharField(max_length=15,choices=CIT_CAT)
    Stay_In_Current_City_Years = models.CharField(max_length=15,choices=STAY)
    Marital_Status = models.IntegerField(default=0)
    Product_Category_1 = models.FloatField(default=0)
    Product_Category_2 = models.FloatField(default=0)
    Product_Category_3 = models.IntegerField(default=0)
    
    def to_dict(self):
        return{
		"User_ID" :self.User_ID,
    		"Product_ID": self.Product_ID,
    		"Gender":self.Gender,
    		"Age": self.Age,
    		"Occupation" : self.Occupation,
    		"City_Category" : self.City_Category,
    		"Stay_In_Current_City_Years" : self.Stay_In_Current_City_Years,
    		"Marital_Status" : self.Marital_Status,
    		"Product_Category_1" : self.Product_Category_1,
    		"Product_Category_2" : self.Product_Category_2,
    		"Product_Category_3" : self.Product_Category_3
	}