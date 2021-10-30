from djongo import models

from encrypted_model_fields.fields import EncryptedCharField


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


class NordigenRequisition(models.Model):
    """
    Trigger function for Mongo DB:
    Needed for creating ID for the model
    how to setup trigger in mongo DB Atlas: https://www.mongodb.com/basics/mongodb-auto-increment
    Trigger name: nordigenRequisitionId

    exports = async function(changeEvent) {
        var docId = changeEvent.fullDocument._id;

        const countercollection = context.services.get("3vial").db(changeEvent.ns.db).collection("counters");
        const authentication_nordigenrequisition = context.services.get("3vial").db(changeEvent.ns.db).collection(changeEvent.ns.coll);

        var counter = await countercollection.findOneAndUpdate({_id: changeEvent.ns },{ $inc: { seq_value: 1 }}, { returnNewDocument: true, upsert : true});
        var updateRes = await authentication_nordigenrequisition.updateOne({_id : docId},{ $set : {id : counter.seq_value}});

        console.log(`Updated ${JSON.stringify(changeEvent.ns)} with counter ${counter.seq_value} result : ${JSON.stringify(updateRes)}`);
        };
    """
    user = models.ForeignKey(UserProfile,related_name='nordigen_requisition', on_delete=models.CASCADE)
    institution_id = EncryptedCharField(max_length=100, blank=True)
    requisition_id = EncryptedCharField(max_length=100, blank=True)
