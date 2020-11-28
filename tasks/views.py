from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Task

# Create your views here.


class HomePage(TemplateView):
    template_name = "home.html"
    model = Task
    context = dict()

    def update_context(self):
        tasks = Task.objects.all()
        if tasks:
            assert isinstance(tasks[0], Task)
        self.context["tasks"] = tasks

    def post(self, request, *args, **kwargs):
        for name, value in request.POST.items():
            if value == "True" and "checked" in name:
                id_ = int(name.replace("checked", ""))
                task_with_id = Task.objects.filter(id=id_).first()
                task_with_id and task_with_id.delete()


        if request.POST['title']:
            Task.objects.create(
                title=request.POST['title'],
                content=request.POST['content'],
                ischecked=request.POST['ischecked'] == "True",
            )

        return redirect("home.html")

    def get(self, request, *args, **kwargs):
        self.update_context()
        return render(request, self.template_name, self.context)
