import faker
import json

fake = faker.Faker()


fakeNames = []
fakeAddresses = []

for i in range(1000):

    fakeNames.append(fake.name())
    fakeAddresses.append(fake.address())

randomNameAddressStore = {'names':fakeNames, 'addresses': fakeAddresses}

f = open('randomNameAddressStore.json', 'w')
f.write(json.dumps(randomNameAddressStore))
f.close()
