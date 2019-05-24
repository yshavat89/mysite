from django.contrib import admin

#Make the poll app modifiable in the admin add 'Question' class

from .models import Question, Choice, Author

class ChoiceInline(admin.TabularInline):# you can use also admin.StackedInline will create diffrent leyout
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently', 'user')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        ('User TYU*()33' , {'fields':['user']}),
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

# without ordering
#admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Author)
