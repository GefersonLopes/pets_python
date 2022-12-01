from rest_framework import serializers;
from groups.serializers import GroupSerializer;
from traits.serializers import TraitSerializer;
from pets.models import Pet;
from groups.models import Group;
from traits.models import Trait;
import ipdb;

class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True);
    name = serializers.CharField();
    age = serializers.IntegerField();
    weight = serializers.FloatField();
    sex = serializers.CharField();
    traits_count = serializers.IntegerField(read_only=True);

    group = GroupSerializer();
    traits = TraitSerializer(many=True);

    def create(self, validated_data: dict):
        group_data = validated_data.pop("group");
        trait_data = validated_data.pop("traits");
        
        group, _ = Group.objects.get_or_create(**group_data);  
        pet = Pet.objects.create(**validated_data, group=group); 
        
        pet.traits_count = len(trait_data);

        for trait in trait_data:
            trait, _ = Trait.objects.get_or_create(**trait);
            pet.traits.add(trait);

        pet.save();    
        return pet;
        
    def update(self, instance: Pet, validated_data: dict):
            
        if "traits" in validated_data:

            traits = validated_data.pop("traits");
            list = [];

            for value in traits:
                trait, _ = Trait.objects.get_or_create(**value);
                list.append(trait);

            instance.traits.set(list)

        if "group" in validated_data: 
            group_data = validated_data.pop("group");
            group,_ = Group.objects.get_or_create(**group_data); 
            instance.group = group;
                

        
        for key, value in validated_data.items():
            setattr(instance, key, value);
        
        instance.save();
        return instance;

