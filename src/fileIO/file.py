#when working is files, it's best to use OS..to maintain functionality on different systems
import os
import yaml

#path to data file
data_filepath = os.path.dirname(os.path.realpath(__file__)) + '/player_data.yaml'

def __read_data():
    #returns the entire yaml
    dictionary = yaml.safe_load(open(data_filepath, 'r'))
    if dictionary is None:
        return {}
    return dictionary

def __write_data(data):
    #writes entire yaml file 
    with open(data_filepath,'w') as file:
        yaml.dump(data, file)


def fetch_user_data(context): 
    #fetches user data given context
    user_name = context.message.author.name + "#" + context.message.author.discriminator
    
    all_data = __read_data()
    user_data = {}

    if user_name not in all_data:
        all_data[user_name] = {}
        __write_data(all_data)
    else:
        user_data = all_data[user_name]

    return user_data

def write_user_data(context, user_data):
    #writes user data given context
    user_name = context.message.author.name + "#" + context.message.author.discriminator
    
    all_data = __read_data()
    all_data[user_name] = user_data

    __write_data(all_data)
    



if __name__ == '__main__':
    print(os.path.dirname(os.path.realpath(__file__)))