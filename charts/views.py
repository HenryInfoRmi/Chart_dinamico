from django.shortcuts import render
from .models import HP,projects,sub_projects
# Create your views here.
def index(request):

    typevar = request.GET.get('type', '')
    if not typevar:
        typevar = 'horizontalBar'
    if typevar == 'horizontalBar':
        axi = "x"
    else:
        axi = "y"


    name_pro = []
    hora_cos_pro = []
    hora_pla_pro = []
    med_hora_pro = []
    med_task_pro = []
    list_hora_cos_sub_pro = []
    list_hora_pla_sub_pro = []
    list_med_hora_sub_pro = []
    list_med_task_sub_pro = []

    

    for project in projects.objects.all():
        

        hp_numeros = HP.objects.filter(project_hp=project.id)
        name_pro.append(project.project_name)
        soma = 0

        for hp_numero in hp_numeros:
            soma = hp_numero.consumed_hours + soma
    
        hora_cos_pro.append(soma)
        
        soma = 0
        
        for hp_numero in hp_numeros:
            soma = hp_numero.planned_hours + soma
        
        hora_pla_pro.append(soma)

        soma = 0

        media = 0

        for hp_numero in hp_numeros:
            soma = hp_numero.consumed_hours_p + soma
        media = soma / len(hp_numeros)
        med_hora_pro.append(media*100)

        soma = 0

        media = 0

        for hp_numero in hp_numeros:
            soma = hp_numero.done_task_p + soma
        media = soma / len(hp_numeros
        )
        med_task_pro.append(media*100)

        soma = 0
        media = 0
        name_sub_pro = []
        hora_cos_sub_pro = []
        hora_pla_sub_pro = []
        med_hora_sub_pro = []
        med_task_sub_pro = []

        for sub_project in sub_projects.objects.all():
        

            hp_numeros = HP.objects.filter(sub_project_hp=sub_project.id,project_hp=project.id)
            name_sub_pro.append(sub_project.sub_project_name)
            soma = 0

            for hp_numero in hp_numeros:
                soma = hp_numero.consumed_hours + soma

            hora_cos_sub_pro.append(soma)

            soma = 0

            for hp_numero in hp_numeros:
                soma = hp_numero.planned_hours + soma

            hora_pla_sub_pro.append(soma)

            soma = 0

            media = 0

            for hp_numero in hp_numeros:
                soma = hp_numero.consumed_hours_p + soma

            if soma:
                media = soma / len(hp_numeros)
            med_hora_sub_pro.append(media*100)

            soma = 0

            media = 0

            for hp_numero in hp_numeros:
                soma = hp_numero.done_task_p + soma
            if soma:
                media = soma / len(hp_numeros)
            med_task_sub_pro.append(media*100)
        
        list_hora_cos_sub_pro.append(hora_cos_sub_pro)
        list_hora_pla_sub_pro.append(hora_pla_sub_pro)
        list_med_hora_sub_pro.append(med_hora_sub_pro)
        list_med_task_sub_pro.append(med_task_sub_pro)




    name_sub_pro = []
    hora_cos_sub_pro = []
    hora_pla_sub_pro = []
    med_hora_sub_pro = []
    med_task_sub_pro = []
    list_hora_cos_pro = []
    list_hora_pla_pro = []
    list_med_hora_pro = []
    list_med_task_pro = []

    for sub_project in sub_projects.objects.all():
        

        hp_numeros = HP.objects.filter(sub_project_hp=sub_project.id)
        name_sub_pro.append(sub_project.sub_project_name)
        soma = 0

        for hp_numero in hp_numeros:
            soma = hp_numero.consumed_hours + soma
    
        hora_cos_sub_pro.append(soma)
        
        soma = 0
        
        for hp_numero in hp_numeros:
            soma = hp_numero.planned_hours + soma
        
        hora_pla_sub_pro.append(soma)

        soma = 0

        media = 0

        for hp_numero in hp_numeros:
            soma = hp_numero.consumed_hours_p + soma
        media = soma / len(hp_numeros)
        med_hora_sub_pro.append(media*100)

        soma = 0

        media = 0

        for hp_numero in hp_numeros:
            soma = hp_numero.done_task_p + soma
        media = soma / len(hp_numeros
        )
        med_task_sub_pro.append(media*100)

        name_pro_fil = []
        hora_cos_pro_fil = []
        hora_pla_pro_fil = []
        med_hora_pro_fil = []
        med_task_pro_fil = []
        for project in projects.objects.all():
        

            hp_numeros = HP.objects.filter(sub_project_hp=sub_project.id,project_hp=project.id)
            name_pro_fil.append(project.project_name)
            soma = 0

            for hp_numero in hp_numeros:
                soma = hp_numero.consumed_hours + soma

            hora_cos_pro_fil.append(soma)

            soma = 0

            for hp_numero in hp_numeros:
                soma = hp_numero.planned_hours + soma

            hora_pla_pro_fil.append(soma)

            soma = 0

            media = 0

            for hp_numero in hp_numeros:
                soma = hp_numero.consumed_hours_p + soma
            if soma:
                media = soma / len(hp_numeros)
            med_hora_pro_fil.append(media*100)

            soma = 0

            media = 0

            for hp_numero in hp_numeros:
                soma = hp_numero.done_task_p + soma
            if soma:
                media = soma / len(hp_numeros)
            med_task_pro_fil.append(media*100)

            soma = 0
            media = 0
        list_hora_cos_pro.append(hora_cos_pro_fil)
        list_hora_pla_pro.append(hora_pla_pro_fil)
        list_med_hora_pro.append(med_hora_pro_fil)
        list_med_task_pro.append(med_task_pro_fil)
        









    return render(request, 'charts/index.html', {
        'name_pro':name_pro,
        'hora_cos_pro' : hora_cos_pro,
        'hora_pla_pro' : hora_pla_pro,
        'med_hora_pro' : med_hora_pro,
        'med_task_pro' : med_task_pro,
        'name_sub_pro':name_sub_pro,
        'hora_cos_sub_pro' : hora_cos_sub_pro,
        'hora_pla_sub_pro' : hora_pla_sub_pro,
        'med_hora_sub_pro' : med_hora_sub_pro,
        'med_task_sub_pro' : med_task_sub_pro,
        'list_hora_cos_sub_pro' : list_hora_cos_sub_pro,
        'list_hora_pla_sub_pro' : list_hora_pla_sub_pro,
        'list_med_hora_sub_pro' : list_med_hora_sub_pro,
        'list_med_task_sub_pro' : list_med_task_sub_pro,
        'list_hora_cos_pro' : list_hora_cos_pro,
        'list_hora_pla_pro' : list_hora_pla_pro,
        'list_med_hora_pro' : list_med_hora_pro,
        'list_med_task_pro' : list_med_task_pro,
        'type':typevar,
        'axi':axi
    })