# list
list is a container to store a set of value of any data type
in a way we can consider it as an array with hetroginious elements/datatype
```python
MyList=["vishwa",101,0.59]
print(MyList)

print(MyList[0])
```
we can use same method in both list and string for getting index of list or character in string

### strings are immutable and list is not
## Example:-
```python
a="omg"
a[1]="n" #Error
```
```python
MyList=["vishwa",101,0.59]
MyList[0]=10 #Sucess
#[10, 101, 0.59]
```
```python
MyList="aman"
MyList.startswith("a") 
```
return if the value is true or false \
if the first value/letter in a word is 'a'
