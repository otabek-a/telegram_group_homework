from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, user_id: str) -> dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (str): User id of the user
    Returns:
        dict: Number of messages of the user
    """
   
    count = 0
    for message in data['messages']:
        if 'text' in message and message.get('user_id') == user_id:  
            count += 1
    return {user_id: count}

# Ma'lumotni bir marta o'qing
data = read_data('data/result.join')

# Foydalanuvchi ID'sini olamiz
user_ids = find_all_users_id(data)

# Agar foydalanuvchilar ro'yxati bo'sh bo'lmasa, xabarlar sonini hisoblaymiz
if user_ids:
    user_id = user_ids[0]  # O'zingizga kerakli foydalanuvchi ID'sini tanlang
    print(find_user_message_count(data, user_id))
else:
    print("Foydalanuvchi ID'si topilmadi.")
