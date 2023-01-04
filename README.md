## Timmy and mountains

# Setup and Installation



## Clone Repository
```
git clone git@github.com:bjvta/timmy-mountain.git && cd timmy-mountain
```


## Install Dependencies
### Add the virtualenv 

```
pip3 install virtualenv
virtualenv env
source env/bin/activate
```

### Install dependencies

```
pip3 install -r requirements.txt
```

## Run Tests
```
pytest
```

## We have three problems that we solve here:
### 1. Check valid mountain

These examples are valid:

```
/\      //\\//\\      ////\\\\           ////\\\/////\\\\\\

                                                   /\
                          /\                /\    /  \
        /\  /\           /  \              /  \  /    \
/\     /  \/  \         /    \            /    \/      \
                       /      \          /              \


```


### 2. Check valid mountain with tunnels


These examples are valid:

```
 />//\\<\           //>/\<\/>/>/\<\<\\

                                 /\   
                                >  <
                        /\     /    \
    /\                 >  <   >      <
   /  \               /     \/        \
  >    <             /                 \
 /      \           /                   \

```

### 3. Return a number of changes to have a valid mountain

These are some examples:

```
/\\                             \///\\

Must return: 1                  Must return: 2

```