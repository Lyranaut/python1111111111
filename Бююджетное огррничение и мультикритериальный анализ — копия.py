#---------------------------Импорт библиотек 
import csv #Модуль csvреализует классы для чтения и записи табличных данных в формате CSV. 
#Это позволяет программистам сказать: «записать эти данные в формате, предпочитаемом Excel», или «прочитать данные из этого файла, 
#созданного Excel», не зная точных деталей формата CSV, используемого Excel.
import numpy as np



n_projects=10   #количество критериев задачи(диапазон, или шаг), где вместо n_projects может быть любое название переменной

ii=np.arange(n_projects)  #создание масива с равномерным расспредеением критериев. ii - переменная масива, np - библиотека с командами.
#arange -создания массивов на основе числовых диапазонов.
projects_cost_arr=np.array(ii,'f')
#Массив, любой объект, предоставляющий интерфейс массива, объект, чей метод __array__ возвращает массив, или любая (вложенная) последовательность.
#'f' - структура памяти масива отвечающая за order parametrs 
projects_cost_arr[:]=0.0 #пустые первоначальные значения масива
projects_title_arr=[] #возврат поэлеметных часей масива(пустой первоначлаьно)
i=0 #параметер шага для цикла
while(i < n_projects): #перебор шагов до количества заданых критриев
  projects_title_arr.append('') #добавление пустых элиментов в масив
  i=i+1 #после каждого шага увиличение параметра шага

#-----------------------------------------
#---------- Load Criteria Table ----------

with open('portfolios_formed-v2_criteria.csv', newline='') as csvfile: #загрузка таблицы критериев из файла portfolios_formed-v2_criteria.csv
#присвоение таблице значение переменной csvfile
  scrit0 = list(csv.reader(csvfile, delimiter=',')) #определение переменной script0 куда мы записываем лист параметров таблицы  script
  #delemiter - параметер листа, который отвечает за розделительный знак между критериями, может иметь любой символ вместо ","

count_row=0 #параметр стобцов, по умолчанию ставим 0
for row_str in scrit0: #цикл по колличеству столбцов в таблице под параметром scritp0
  n_col=len(row_str) #запись длинны столбцов в перемнную n_col
  n_crit=n_col-2 # n критерий с значением длинны столбцов - 2
  if (count_row == 0): #проверяем количесво сттолбцов на равность 0
    n_crit0=n_crit #если равно, создаём n_crit0=n_crit
    ii=np.arange(n_projects*n_crit).reshape(n_projects,n_crit) #изменение формы масива n_projects*n_crit -> на проэкты-критерии
    criteria_arr=np.array(ii,'f')    
#Массив, любой объект, предоставляющий интерфейс массива, объект, чей метод __array__ возвращает массив, или любая (вложенная) последовательность.
#'f' - структура памяти масива отвечающая за order parametrs  
    criteria_arr[:,:]=0.0 #ОПРЕДЕЛЕНИЕ критериев массива

  if (n_crit != n_crit0): #проверка неравности n_crit=n_crit0, если не равны то:
    print("Wrong list counting for criteria. Exiting.")
    break
  sx=row_str[0] #создаём переменную sx которой присаеваем нулевой критерий 
  if (count_row == 0): #снова проверяем количесво сттолбцов на равность 0
    criteria_title_arr=[] #параметры масива
    i=2 #определяем параметр - = 2
    while (i < n_col): #увеличиваем параметр i на один шаг. пока не будет привышено длинну столбца
      criteria_title_arr.append(row_str[i]) #заполнение пустых элементов масива параметром i
      i=i+1 #увеличение шага

  ix=-1
  if (sx == 'A'): ix=0
  if (sx == 'B'): ix=1
  if (sx == 'C'): ix=2
  if (sx == 'D'): ix=3
  if (sx == 'E'): ix=4
  if (sx == 'F'): ix=5
  if (sx == 'G'): ix=6
  if (sx == 'H'): ix=7
  if (sx == 'I'): ix=8
  if (sx == 'J'): ix=9
  if (ix >= 0):
    projects_title_arr[ix]=sx #если ix >= 0 присваеваем ix элементу масива значение sx
    projects_cost_arr[ix]=float(row_str[1]) #возврат числа с плавающей запятой для 1 параметра масиве
    i=0
    while (i < n_crit):
      criteria_arr[ix,i]=float(row_str[i+2])#возврат числа с плавающей запятой для i+2 параметра масиве
      i=i+1 #шаг

  if (sx == 'criteria weights'):
    ii=np.arange(n_crit) #присвоение ii масив из критериев n_crit
    criteria_weights_arr=np.array(ii,'f')
#Массив, любой объект, предоставляющий интерфейс массива, объект, чей метод __array__ возвращает массив, или любая (вложенная) последовательность.
#'f' - структура памяти масива отвечающая за order parametrs  
    criteria_weights_arr[:]=1.0 #ОПРЕДЕЛЕНИЕ критериев массива
    i=2 
    while (i < n_col):
      criteria_weights_arr[i-2]=float(row_str[i]) #возврат числа с плавающей запятой для i параметра масива при i-2
      i=i+1 #шаг


  print("n_crit:",count_row,n_col) #вывод: n_crit: строка и столбец масива
  count_row=count_row+1 #увеличение строки на 1


print("criteria_title_arr:",len(criteria_title_arr),n_crit) #criteria_title_arr: длинна критериев
print("criteria_title_arr:",criteria_title_arr) #параметр масива
print("criteria_arr:",criteria_arr.shape) #возврат формы масива
fmt="{:.2f}" #формат синтаксиса с двумя фиксированнными точками.
ix=0
while (ix < n_projects): #переборка ix параметра до количества критержиев
  print(projects_title_arr[ix],projects_cost_arr[ix]," : ",criteria_arr[ix,:]) #вывод пвраметров
  ix=ix+1 #увеличение шага

#---------- End Load Criteria Table ----------
#---------------------------------------------


#по анологии с таблицей критериев загружаем измененную set tablr
#------------------------------------
#---------- Load Set Table ----------

with open('portfolios_formed-v2_sets.csv', newline='') as csvfile:
#  spamreader = csv.reader(csvfile, delimiter=',')
  sdata0 = list(csv.reader(csvfile, delimiter=','))
#  for row in spamreader:
#    print(', '.join(row))

n_sets=len(sdata0)
print("Number of sets: ",n_sets)
print(sdata0[0][1])

set_arr = np.arange(n_sets*n_projects).reshape(n_sets,n_projects)
set_arr[:,:]=0
#print(set_arr)
print("set_arr:",set_arr.min(),set_arr.max())
#print(set_arr)

count_row=0
for row_str in sdata0:
  sx=row_str[0]
#  print(sx,int(sx)-1,count_row)
  if ((int(row_str[0])-1) != count_row):
    print("Wrong list counting. Exiting.")
    exit()

  for sx in row_str:
    ix=-1
    if (sx == 'a'): ix=0
    if (sx == 'b'): ix=1
    if (sx == 'c'): ix=2
    if (sx == 'd'): ix=3
    if (sx == 'e'): ix=4
    if (sx == 'f'): ix=5
    if (sx == 'g'): ix=6
    if (sx == 'h'): ix=7
    if (sx == 'i'): ix=8
    if (sx == 'j'): ix=9
    if (ix >= 0): set_arr[count_row,ix]=1

  count_row=count_row+1
#  if (count_row > 2): break

print("set_arr:",set_arr.min(),set_arr.max())
print("set_arr:",set_arr[0,:])
print("set_arr:",set_arr[12,:])
#---------- End Load Set Table ----------
#----------------------------------------



#======================================
#========== Start Processing ==========
indexes_set=np.arange(n_sets) # indexes_set is array of indexes for the first dimension in set_arr, i.e. initially their values goes from 0 to n_set-1
set_cumulative_criteria=np.array(ii,'f')
set_cumulative_criteria[:]=0.0
print("indexes_set: ",len(indexes_set))
#exit()

icount_bubble=0
while (icount_bubble < n_sets):
  ix=0
  while (ix < n_sets-1):
    ix1=indexes_set[ix]
    ix2=indexes_set[ix+1]
    dominance_switch=0
#  compare set_arr[ix1,:] and set_arr[ix2,:]
#  here is your test algorithm
#  dominance_switch=0 (no switch, i.e, set_arr[ix1,:] dominates set_arr[ix2,:])
#  dominance_switch=1 (switch, i.