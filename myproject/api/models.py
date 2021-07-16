
from django.db import models
from django.contrib.auth.models import User




class nodes(models.Model):
    name = models.CharField(max_length=200,
                            unique=True 
                              )
    type = models.CharField(max_length=200,
                            default = "IOTA node" 
                              )

    
    def __str__(self):
        return self.name

class inputs(models.Model):
    input = models.CharField(max_length=200,
                              )
    tt = models.CharField(max_length=200,
    blank = True, null= True,
                            unique=True
                              )
    # node = models.ForeignKey(nodes, on_delete=models.CASCADE,
    #                           blank = True, null= True
    #                          )
    #problem = models.ForeignKey(problem, on_delete=models.CASCADE
    #                         )               
    def __str__(self):
        return self.input

class outputs(models.Model):
    output = models.CharField(max_length=200,
    blank = True, null= True
          
                )
    problem = models.ForeignKey("problem", on_delete=models.CASCADE,
                              blank = True, null= True
                             ) 
    

    input = models.ForeignKey(inputs, on_delete=models.CASCADE
                            )               
    node = models.ForeignKey(nodes, on_delete=models.CASCADE,
                              blank = True, null= True
                             )
     

class problem(models.Model):
    problem_tag= models.CharField(max_length=200,
                                  blank = True, null= True
                              )
    
    # proccessor = models.ForeignKey(nodes, on_delete=models.CASCADE,
    #                           blank = True, null= True
    #                                    )
    
    input = models.ManyToManyField("inputs", through='outputs')
    final_answer = models.CharField(max_length=200,
                                   default="not computed"
                                  )
    # output =  models.CharField(max_length=200,
    #                            null = True, blank=True
    #                           )
    def __str__(self):
       return  self.final_answer