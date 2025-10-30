def calculate_hand_value(hand: list[dict]):
    value=0
    total=0
    for i in hand:
        if i['rank'] == '2'or i['rank'] =='3'or i['rank'] =='4'or i['rank'] =='5'or i['rank'] =='6'or i['rank'] =='7'or i['rank'] =='8'or i['rank'] =='9'or i['rank'] =='10':
            value=int(i['rank'])
        elif i['rank']=='j' or i['rank']=='q' or i['rank']=='k':
            value=10
        elif i['rank']=='a':
            value=1
        total += value
    return total

def deal_two_each(deck: list[dict], player: dict, dealer: dict):
    player={'hand':[deck[-1],deck[-2]]}
    dealer={'hand':[deck[-3],deck[-4]]}
    deck.pop()
    deck.pop()
    deck.pop()
    deck.pop()
    total_player=calculate_hand_value(player)
    total_dealer = calculate_hand_value(dealer)
    print(f'total_player{total_player}')
    print(f'total_dealer{total_dealer}')




def run_full_game(deck, player, dealer):
    deal_two_each(deck, player, dealer)
