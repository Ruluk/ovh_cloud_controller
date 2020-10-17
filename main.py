import ovh

client = ovh.Client()

if __name__ == '__main__':
    print("Welcome", client.get('/me'))
