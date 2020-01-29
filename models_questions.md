
1.What does a model’s field type represent? If I use a CharField versus a TextField, for example, what does that change about how the data is stored?

The documentation says that CharField() should be used for smaller strings and TextField() should be used for larger strings.

2.What is the difference between the null and blank field options? What do each of them represent?

Null field is absent of any data. a blank field is like an empty string.
null is purely database-related, whereas blank is validation-related. If a field has blank=True , validation on Django's admin site will allow entry of an empty value. If a field has blank=False , the field will be required.


3.How do we use the TextChoices field type to display multiple options?

On the selected model we can use TextChoices to display a list of options that can be accessed. ?

4.What is a primary_key field? If we don’t specify a primary key, what is the default?

The primary_key is the way the database assigns a key to the value.
primary_key is defaulted to True. unless it is overwritten

5.How do we specify a verbose name? What purpose does it serve?

a verbose name is an optional first positional argument that sets the key for the objects feild.?

6.In the documentation under “Many-to-one Relationships”, an example is given of “Manufacturer” and “Car” models. Complete the code by adding at least 2 new fields to each model.

nationality = models.ForeignKey(Nation, on_delete=models.CASCADE)
legal_in_USA = models.ForeignKey(Legal, on_delete=models.CASCADE)

car_type = models.ForeignKey(Type, on_delete=models.CASCADE)
car_color = models.ForeignKey(Color, on_delete=models.CASCADE)




7.In the documentation under “Many-to-Many Relationships”, an example is given of “Pizza” and “Topping” models. Complete the code by adding at least 2 new fields to each model.

cheese = models.ManyToManyField(cheese)
other_toppings = models.ManyToManyField(Other)

sauce = models.ManyToManyField(sauce)
crust = models.ManyToManyField(Crust)


8.What is an example of a one-to-one relationship? When would we use a OneToOneField?

A one to one relationship could be used in ragards to passwords or user IDs

9.Sometimes we need to relate a model to one from another app. Give an example of an import line to show how we’d import the other model.

To do this, import the related model at the top of the file where your model is defined. Then, refer to the other model class wherever needed

from this.py import that

10.What is the class Meta? When would we use it?

No idea. I dont understand what the documentation is saying about it.

11.What is an example of a model method? Suppose we have a class Album. What methods might we want to write for it?



12.Give an example of model inheritance. How does inheritance help us to write better code?

Keeps us DRY
