import yaml

# execução no main
if __name__ == '__main__':
    # abrindo file yaml
    stream = open('test.yaml', 'r')

    # convertendo arquivo para yaml
    dictionary = yaml.safe_load(stream)

    # iterando yaml
    for key, value in dictionary.items():
        print(f'{key}: {str(value)}')
