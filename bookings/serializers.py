from rest_framework import serializers

class AppointmentSerializer(serializers.Serializer):

    patient_name=serializers.CharField()
    phone=serializers.CharField()
    doctor=serializers.IntegerField()
    appointment_date=serializers.DateField()
    token_number=serializers.IntegerField(read_only=True)
    appointment_time=serializers.TimeField(read_only=True)
    problem=serializers.CharField()
    created_at=serializers.DateTimeField(read_only=True)
    
