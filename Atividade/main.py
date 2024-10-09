import os 
import sys
sys.path.append('/workspaces/Atividade_Em_Dupla')
from Atividade.models.funcionario import Funcionario
from Atividade.models.medico import Medico
from Atividade.models.engenheiro  import Engenheiro
from Atividade.models.endereco import Endereco


os.system("cls || clear")

funcionario1 = Funcionario("Icaro", "071988998", "Icaro@gmail...", 1500, Endereco("Rua A", "123", "1 Andar", "4445-221", "Salvador"))
medico1 = Medico("Rafael", "071877871", "Rafael@gmail...", 2500, Endereco("Rua B", "266", "2 Andar", "4454-211", "Salvador"),"999")
engenheiro1 = Engenheiro("Jonas", "0719899897", "Jonas@gmail...", 3500, Endereco("Rua C", "266", "3 Andar", "6665-544", "Salvador"),"888")

print(funcionario1)
print(medico1)
print(engenheiro1)