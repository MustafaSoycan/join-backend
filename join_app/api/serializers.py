from rest_framework import serializers
from join_app.models import Contact, Task


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    subtasks = serializers.ListField(
        child=serializers.CharField(),
        required=False,  # Falls es optional ist
        allow_null=True   # Falls es null sein kann
    )

    assigned_to_details = ContactSerializer(
        source='assigned_to', many=True, read_only=True)

    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = Task
        fields = '__all__'
