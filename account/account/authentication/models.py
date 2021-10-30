from django import forms
from djongo import models

from encrypted_model_fields.fields import EncryptedCharField


# class Requisition(models.Model):
#     institution_id = models.CharField(max_length=100, primary_key=True)
#     requisition = models.CharField(max_length=100, )
#
#     class Meta:
#         managed=False
#
#     def __str__(self):
#         return self.institution_id
#
#
# class RequisitionForm(forms.ModelForm):
#     class Meta:
#         model = Requisition
#         fields = '__all__'


class UserProfile(models.Model):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)

    user_identifier = models.CharField(max_length=40, blank=False)
    base_currency = models.CharField(max_length=5, default='GBP')
    source_label = models.CharField(max_length=20, blank=True)

    # Binance access
    binance_key = EncryptedCharField(max_length=200, blank=True)
    binance_secret = EncryptedCharField(max_length=200, blank=True)

    # Coinbase access
    coinbase_api_secret = EncryptedCharField(max_length=200, blank=True)
    coinbase_api_key = EncryptedCharField(max_length=200, blank=True)
    coinbase_api_pass = EncryptedCharField(max_length=200, blank=True)

    # Yodlee access
    yodlee_login_name = EncryptedCharField(max_length=200, blank=True,)

    # Nordigen access
    # nordigen_requisitions = models.EmbeddedField(model_container=Requisition, blank=True)

    # Custom Assets
    custom_assets_key = EncryptedCharField(max_length=500, blank=True)

    objects = models.DjongoManager()

    # Maybe it will be better bellow logic to be moved to views but then. On every first GET or PUT we write in the database !
    # We can use user_indentifier which is unique for yodlee_login_name. The same is valid for custom_assets_key. This field is not even needed.
    # def save(self, *args, **kwargs):
    #     # self.yodlee_login_name = self.user_identifier + str(self.id)
    #     # self.custom_assets_key = str(self.id) + self.user_identifier + str(self.id)
    #     self.nordigen_requisitions['institution_id']='5'
    #     super(UserProfile, self).save(*args, **kwargs)


class NordigenRequisition(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    institution_id = models.CharField(max_length=100, null=True)
    requisition_id = models.CharField(max_length=100, null=True)

"""
Triger function for Mongo DB:
Triger name: nordigenRequisitionId

exports = async function(changeEvent) {
    var docId = changeEvent.fullDocument._id;
    
    const countercollection = context.services.get("3vial").db(changeEvent.ns.db).collection("counters");
    const authentication_nordigenrequisition = context.services.get("3vial").db(changeEvent.ns.db).collection(changeEvent.ns.coll);
    
    var counter = await countercollection.findOneAndUpdate({_id: changeEvent.ns },{ $inc: { seq_value: 1 }}, { returnNewDocument: true, upsert : true});
    var updateRes = await authentication_nordigenrequisition.updateOne({_id : docId},{ $set : {id : counter.seq_value}});
    
    console.log(`Updated ${JSON.stringify(changeEvent.ns)} with counter ${counter.seq_value} result : ${JSON.stringify(updateRes)}`);
    };
"""