from rest_framework import serializers
from provider_serializer import ProviderSerializer


class NomenclatureSerializer(serializers.Serrializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=256)
    selling_price = serializers.DecimalField()
    created_by = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    provider = ProviderSerializer()
    

# nomenclature: {
#   id: 1,
#   name: 'Конфэта',
#   selling_price: 500.0,
#   created_by: 1,
#   created_at: '2023-05-18 09:30:00',
#   updated_at: '2023-05-18 09:30:00',
#   provider: [ 
#       {
#           id: 1,
#           title: 'ИП Дечевян А.В.',
#           requisits: {
#               id: 1,
#               ...
#           },
#           contacts: {
#               id: 1,
#               ...
#           }
#       },
#       {
#           id: 2,
#           title: 'ИП Гончарян А.Ю.',
#           requisits: {
#               id: 2,
#               ...
#           },
#           contacts: {
#               id: 2,
#               ...
#       },
#   ]
# }
