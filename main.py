import asyncio
import aminofix.asyncfix
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.RED+ Style.BRIGHT)
print(pyfiglet.figlet_format("KWEL ATE YOUR PIZZA", font="big"))
client = aminofix.asyncfix.Client()
print("\t\033[1;32m Follow Spam \033[1;36mKWEL \n\n")
async def authorization():
    try:
        await client.login(email=input("°•°•°Email >> "), password=input("°•°•°Password >> "))
    except Exception as e:
        print(e)
        await authorization()


async def choice_community():
    try:
        clients = (await client.sub_clients(start=0, size=100))
        for x, name in enumerate(clients.name, 1):
            print(f"{x}.{name}")
        com_id = clients.comId[int(input("°•°•°Choice community >> ")) - 1]
        return com_id
    except ValueError as e:
        print(f"Error: {e}")


async def follow_spam(user_ids, sub_client):
    await sub_client.follow(user_ids)
    print("online users getting spam")


async def main():
    await authorization()
    com_id = await choice_community()
    sub_client = aminofix.asyncfix.SubClient(comId=com_id, profile=client.profile)
    user_ids = (await sub_client.get_online_users(start=0, size=100)).profile.userId
    task_count = int(input(" •°•°•°How many times >>  "))
    while True:
        try:
            await asyncio.gather(*[asyncio.create_task(follow_spam(user_ids=user_ids,
                                                                   sub_client=sub_client))
                                   for _ in range(task_count)])
        except Exception as e:
            print(e)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
