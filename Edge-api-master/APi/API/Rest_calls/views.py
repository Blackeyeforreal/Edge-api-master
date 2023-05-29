from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets,views,permissions , generics,response,authentication
from django.contrib.auth import login,logout
from .serializers import ChallengeSerializer, UserSerializer, Loginserializer
from .models import Users
from django.core.files import File

import json
from pathlib import Path 
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import requires_csrf_token, ensure_csrf_cookie, csrf_protect
# Create your views here.
from django.contrib.auth.models import User, Group 
from .misc.AI_model import calculate_outcome, calculate_probabilities
from rest_framework import viewsets 
from rest_framework import permissions
from Rest_calls.serializers import UserSerializer, PlayerSerializer , GroupSerializer, TeamSerializer
from .models import CricketPlayer,CricketTeam, Challenges, PlayerEleven, BowlingLineUp
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
   
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser
from rest_framework.decorators import APIView, api_view
from django.conf import settings

import random
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie
ensure_csrf = method_decorator(ensure_csrf_cookie)
csrf_protect_method = method_decorator(csrf_protect)
class setCSRFCookie(APIView):
    permission_classes = []
    authentication_classes = []
    @ensure_csrf
    def get(self, request):
        return Response("CSRF Cookie set.")
    
class CreatTeam(APIView):
    authentication_classes=[ SessionAuthentication ]
    permission_classes = [IsAuthenticated]
   
    # queryset = CriketPlayer.objects.all()
    # serializer_class = PlayerSerializer
    # permission_classes = [permissions.IsAdminUser]
    parser_classes = [JSONParser ,MultiPartParser]
   
    def creatPlayer (self,request, TeamID):
        
        F_name =[ 'John', 'Emma', 'Oliver', 'Ava', 'William', 'Sophia', 'James', 'Isabella', 'Benjamin', 'Mia',
    'Lucas', 'Charlotte', 'Henry', 'Amelia', 'Alexander', 'Harper', 'Michael', 'Evelyn', 'Daniel', 'Abigail',
    'Elijah', 'Emily', 'Matthew', 'Elizabeth', 'Joseph', 'Sofia', 'David', 'Avery', 'Samuel', 'Ella',
    'Jackson', 'Scarlett', 'Sebastian', 'Grace', 'Jack', 'Chloe', 'Andrew', 'Victoria', 'Owen', 'Riley',
    'Joseph', 'Luna', 'Gabriel', 'Lily', 'Anthony', 'Layla', 'Carter', 'Penelope', 'Jayden', 'Zoey',
    'Dylan', 'Nora', 'Luke', 'Lillian', 'Henry', 'Zoe', 'Isaac', 'Mila', 'Wyatt', 'Aria',
    'Caleb', 'Eleanor', 'Nathan', 'Hannah', 'Ryan', 'Aubrey', 'Adrian', 'Addison', 'Christian', 'Stella',
    'Mason', 'Natalie', 'Eli', 'Leah', 'Jonathan', 'Willow', 'Landon', 'Lucy', 'Julian', 'Savannah',
    'Hunter', 'Brooklyn', 'Aaron', 'Audrey', 'Charles', 'Claire', 'Evan', 'Hazel', 'Thomas', 'Aaliyah',
    'Nicholas', 'Skylar', 'Isaiah', 'Ellie', 'Adam', 'Violet', 'Alex', 'Bella', 'Josiah', 'Aurora'
]
        S_name = [
    'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
    'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson',
    'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King',
    'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter',
    'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins',
    'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Bailey',
    'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Ramirez',
    'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross',
    'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington',
    'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz', 'Hayes'
]
        for batsmen in range(1,8):
            name = random.choice(F_name ) + random.choice(S_name)
            if ( batsmen<3):
                SpinVstar= random.randrange(7,10)
                paceVstar= random.randrange(7,10)
            elif ( batsmen< 6):
                SpinVstar= random.randrange(5,7)
                paceVstar= random.randrange(5,7)
            elif ( batsmen< 8):
                SpinVstar= random.randrange(3,5)
                paceVstar= random.randrange(3,5)
            elif batsmen< 10:
                star = random.randrange (3,6)
            bats_bowling = random.randrange
            instance = CricketPlayer(name = name, age = random.randrange(18, 24), handed = random.choice(['left', 'right']) , bowlingtype = random.choice(['fast','medium','off-spin', 'leg-spin']), battingVspin = SpinVstar, battingVpace = paceVstar,bowling = 6, experience = random.randrange(3-6) , fielding = random.randrange(4, 8),TeamID = TeamID)
            instance.save()

        for bowler in range(1,8):
            name = random.choice(F_name ) + random.choice(S_name)
            bowler_type = random.choice(['fast','medium','off-spin', 'leg-spin'])
            if ( bowler <3 ):
                stars = random.randrange(7,10)
            elif bowler<6 : 
                stars = random.randrange(5,7)
            else:
                stars = random.randrange(3,5)
            instance = CricketPlayer(name = name, age = random.randrange(18, 24), handed = random.choice(['left', 'right']) , bowlingtype = bowler_type, battingVspin = random.randrange(1,3) , battingVpace = random.randrange(1,3),bowling = stars , experience = random.randrange(3-6) , fielding = random.randrange(4, 8),TeamID = TeamID)
            instance.save()

        for allrounders in range ( 3 ):
            name = random.choice(F_name ) + random.choice(S_name)

            batting_stars = random.randrange(5-9)
            bowlling_stars = random.randrange(5- 9)
            instance = CricketPlayer(name = name, age = random.randrange(18, 24), handed = random.choice(['left', 'right']) , bowlingtype = bowler_type, battingVspin = batting_stars , battingVpace = random.randrange(5,9),bowling = bowlling_stars , experience = random.randrange(3-6) , fielding = random.randrange(4, 8), TeamID = TeamID)
            instance.save()
            
    
    @ensure_csrf_cookie
    @api_view(['GET', 'POST'])
    def team( request, format = "jpg"):
        print("worked fine")
        if request.method == 'POST' or request.method== 'PUT':
            request.data["userId"] = request.user.id
            request.data['userName']= request.user.name
            serializer = TeamSerializer(data=request.data)

            print(serializer,request.data['userName'],request.user.name,request.user)
            print(serializer.is_valid())
            print(serializer._errors)
            teamName = serializer.validated_data.get("teamName")
            
            
           
            if serializer.is_valid():
                serializer.save()
                team= CricketTeam.objects.filter(teamName = teamName  )
                team[0].userName = request.user.name
                #team[0].userId = request.user
                print(team[0].userName,request.user.name)
                
                team[0].save()
               # team.teamImage = request.FILES['file']
                F_name =[ 'John', 'Emma', 'Oliver', 'Ava', 'William', 'Sophia', 'James', 'Isabella', 'Benjamin', 'Mia',
                'Lucas', 'Charlotte', 'Henry', 'Amelia', 'Alexander', 'Harper', 'Michael', 'Evelyn', 'Daniel', 'Abigail',
                'Elijah', 'Emily', 'Matthew', 'Elizabeth', 'Joseph', 'Sofia', 'David', 'Avery', 'Samuel', 'Ella',
                'Jackson', 'Scarlett', 'Sebastian', 'Grace', 'Jack', 'Chloe', 'Andrew', 'Victoria', 'Owen', 'Riley',
                'Joseph', 'Luna', 'Gabriel', 'Lily', 'Anthony', 'Layla', 'Carter', 'Penelope', 'Jayden', 'Zoey',
                'Dylan', 'Nora', 'Luke', 'Lillian', 'Henry', 'Zoe', 'Isaac', 'Mila', 'Wyatt', 'Aria',
                'Caleb', 'Eleanor', 'Nathan', 'Hannah', 'Ryan', 'Aubrey', 'Adrian', 'Addison', 'Christian', 'Stella',
                'Mason', 'Natalie', 'Eli', 'Leah', 'Jonathan', 'Willow', 'Landon', 'Lucy', 'Julian', 'Savannah',
                'Hunter', 'Brooklyn', 'Aaron', 'Audrey', 'Charles', 'Claire', 'Evan', 'Hazel', 'Thomas', 'Aaliyah',
                'Nicholas', 'Skylar', 'Isaiah', 'Ellie', 'Adam', 'Violet', 'Alex', 'Bella', 'Josiah', 'Aurora'
                ]
                S_name = [
                'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
                'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson',
                'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King',
                'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter',
                'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins',
                'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Bailey',
                'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Ramirez',
                'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross',
                'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington',
                'Butler',]
                TeamID = team[0]

                for batsmen in range(1,8):
                    name = random.choice(F_name ) + random.choice(S_name)
                    if ( batsmen<3):
                        SpinVstar= random.randrange(7,10)
                        paceVstar= random.randrange(7,10)
                    elif ( batsmen< 6):
                        SpinVstar= random.randrange(5,7)
                        paceVstar= random.randrange(5,7)
                    elif ( batsmen< 8):
                        SpinVstar= random.randrange(3,5)
                        paceVstar= random.randrange(3,5)
                    elif batsmen< 10:
                        star = random.randrange (3,6)
                    bats_bowling = random.randrange
                    instance = CricketPlayer(Name = name, age = random.randrange(18, 24), handed = random.choice(['left', 'right']) , bowlingtype = random.choice(['fast','medium','off-spin', 'leg-spin']), battingVspin = SpinVstar, battingVpace = paceVstar,bowling = 3 , experience = random.randrange(3,6) , fielding = random.randrange(4, 8),TeamId = TeamID)
                    instance.save()

                for bowler in range(1,8):
                    name = random.choice(F_name ) + random.choice(S_name)
                    bowler_type = random.choice(['fast','medium','off-spin', 'leg-spin'])
                    if ( bowler <3 ):
                        stars = random.randrange(7,10)
                    elif bowler<6 : 
                        stars = random.randrange(5,7)
                    else:
                        stars = random.randrange(3,5)
                    instance = CricketPlayer(Name = name, age = random.randrange(18, 24), handed = random.choice(['left', 'right']) , bowlingtype = bowler_type, battingVspin = random.randrange(1,3) , battingVpace = random.randrange(1,3),bowling = stars , experience = random.randrange(3,6) , fielding = random.randrange(4, 8),TeamId = TeamID)
                    instance.save()

                for allrounders in range ( 3 ):
                    name = random.choice(F_name ) + random.choice(S_name)

                    batting_stars = random.randrange(5,9)
                    bowlling_stars = random.randrange(5, 9)
                    instance = CricketPlayer(Name = name, age = random.randrange(18, 24), handed = random.choice(['left', 'right']) , bowlingtype = bowler_type, battingVspin = batting_stars , battingVpace = random.randrange(5,9),bowling = bowlling_stars , experience = random.randrange(3,6) , fielding = random.randrange(4, 8), TeamId = TeamID)
                    instance.save()
            
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("better luck next time")
    

    @api_view(['GET'])
    def viewPlayers(request   ):
        if request.method == 'GET':
            #team = CreatTeam.objects.filter( userId = request.user)
            print(request.user)
            teamMembers  = CricketPlayer.objects.filter(TeamId =CricketTeam.objects.get(userId = request.user) )
            print(teamMembers)
            
            serializer = PlayerSerializer(teamMembers, many = True)
          
            
            # if not serializer.is_valid():
            #     print (serializer.errors) 
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("better luck next time")



        
        
# class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
#     def enforce_csrf(self, request):
#         return

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    queryset = Users.objects.all().order_by('name')
    serializer_class = UserSerializer

    




class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    @csrf_protect_method
    def post(self, request):
        serializer = Loginserializer(data=request.data,context={'request': request})  
        serializer.is_valid(raise_exception=True) 
        user = serializer.validated_data['user']
        login(request, user)
        #backend mai password re introduce karo
        
        return response.Response(UserSerializer(user).data)
    
    
    
class LogoutView(views.APIView):
    authentication_classes=[ SessionAuthentication ]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        print(request.user)
        logout(request)
        #backend mai password re introduce karo
        
        return Response("logout")
    
class TeamOperation(views.APIView):
    authentication_classes=[ SessionAuthentication ]
    permission_classes = [IsAuthenticated]

    @api_view(['GET'])
    def search_team( request, query):
        serializer = 0
        queryset = CricketTeam.objects.filter( teamName__startswith= query).values()
        print(len(queryset)==1)
        
        serializer = TeamSerializer(queryset, many = True)
        
        # if not serializer.is_valid():
        #     print (serializer.errors) 
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GamePlay(APIView):
    authentication_classes=[ SessionAuthentication ]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser ]

    @ensure_csrf_cookie
    @api_view([ 'POST','GET'])
    def match(request):
        sup_dic = []
       
        challenger = [request.data["challenger_team_id"] , request.data["challenged_team_id"]]
        # Eleven_players = request.data["selectedPlayers"] 

        # for i in range(20):
        #     bowlers.append( CricketPlayer.objects.get(id = request.data["overSelection"][i]) )


        oldtarget = 1000
        
        for i in range(2):
            Eleven_players = []
            bowlers = []
            user_id = CricketTeam.objects.get(id = challenger[i]).userId
            #print(Challenges.objects.get(challenge_id=  request.data["challenge_id"]), user_id)
            Eleven_players_id = PlayerEleven.objects.filter( challenge_id__challenge_id =   request.data["challenge_id"] ,  user_id__id=  user_id.id)
            bowlers_id =  BowlingLineUp.objects.filter(  challenge_id__challenge_id =   request.data["challenge_id"], user_id=user_id)
            for i in range(20):
                bowlers.append( CricketPlayer.objects.get( id = bowlers_id[i].player_id) )
            #print("wroking")
            for i in range(11):
                Eleven_players.append( CricketPlayer.objects.get(id =Eleven_players_id[i].player_id) )
            
        
        
            target = oldtarget
            current_wickets = 0
            current_striker_index = 0
            current_nonStriker_index = 1
            current_bowler_index = 0
            current_runs = 0
        
            wicket_fallen = False 
            #bowling types = fast / medium /off spin / leg spin
            for turn in range(1,121):
                over_no = turn//6
                bowl_type = ""
                bowler_type =  bowlers[current_bowler_index].bowlingtype #["bowlingtype"]

                if ( bowler_type == "fast" or bowler_type =="medium"):
                    bowl_type = "battingVpace"
                else:
                    bowl_type = "battingVspin"
                current_bowler_index = over_no -1
               
                #striker_rating= Eleven_players[current_striker_index][bowl_type]
                striker_rating = Eleven_players[current_striker_index].battingVspin if bowl_type != "battingVpace" else Eleven_players[current_striker_index].battingVpace
                if ( bowl_type == "battingVpace") :
                    bowler_rating = bowlers[current_bowler_index].battingVpace #[bowl_type]
                else:
                    bowler_rating = bowlers[current_bowler_index].battingVspin

                #bowler_rating = bowlers[current_bowler_index].bowl_type #[bowl_type]
                outcome = 9
                while ( outcome>8):
                    prob = calculate_probabilities(striker_rating,bowler_rating)
                    outcome = calculate_outcome(prob)
                
            
                if ( outcome == -1 ):
                    current_wickets +=1 
                    wicket_fallen = True 
                else:
                    current_runs += (outcome - 1 )

                
                
                dic = {
                        'over_no' : over_no,
                        'ball_no' :  6 if turn%6 ==0 else turn%6,
                        "striker" : Eleven_players[current_striker_index].Name,
                        "bowler" : bowlers[current_bowler_index].Name,
                        "striker_rating": Eleven_players[current_striker_index].battingVspin if bowl_type != "battingVpace" else Eleven_players[current_striker_index].battingVpace,
                        "bowler_rating": bowlers[current_bowler_index].battingVpace if bowl_type == "battingVpace" else bowlers[current_bowler_index].battingVspin,
                        "current_runs":current_runs,
                        "non_striker ": Eleven_players[current_nonStriker_index].Name ,
                        "target": target,
                        "wickets_fallen" : current_wickets,
                        "runs_scored_on_current_ball" : outcome -1 ,
                        "total_run": current_runs 
                        }
               
                sup_dic.append(dic)
                if wicket_fallen  :
                    current_striker_index +=1 

                # elif wicket_fallen:
                #     old_index = current_striker_index
                #     current_striker_index = current_nonStriker_index
                #     current_nonStriker_index = old_index + 1 

                if outcome != -1 and outcome%2:
                    current_striker_index , current_nonStriker_index = current_nonStriker_index , current_striker_index

                if dic["ball_no"] == 6 :
                    current_striker_index , current_nonStriker_index = current_nonStriker_index , current_striker_index
                
                if current_wickets == 10:
                    break
                if current_runs>target:
                    break 


            oldtarget =  current_runs
            
          

        match_json = json.dumps( sup_dic)
    
        #to save the json file  
            #file_path = settings.BASE_DIR / 'rest_calls' / 'matchs' / str(request.data["challenge_id"])+'_challenger_'+str(i)
        file_path = Path(settings.BASE_DIR, 'rest_calls', 'matchs', str(request.data["challenge_id"])+'_challenger' +'.json')
        with open(file_path, 'w') as file:
            myfile = File(file)
            myfile.write(match_json)
            myfile.close   


        return Response( "done",status=status.HTTP_201_CREATED)
    @ensure_csrf_cookie
    @api_view([ 'POST','GET'])
    def match_data(request):
        file_path = Path(settings.BASE_DIR, 'rest_calls', 'matchs', str(request.data["challenge_id"])+'_challenger' +'.json')
        with open(file_path) as f:
            data = json.load(f)
            print(data)
            f.close
            return Response(data, status= status.HTTP_201_CREATED,content_type='application/json')

    @api_view([ 'POST'])
    def save_lineup(request):
        
#       
        #dictionary of all the eleven players
        #CricketPlayer.objects.get(id = request.data["overSelection"][index_of_over])  use this to get the specific bowling guy
        #print(data, type(data),"working")
        for i in range (11):
            players = PlayerEleven( user_id = request.user, challenge_id = Challenges.objects.get(challenge_id =request.data["challenge_id"])  , player_id =request.data["selectedPlayers"][i]["id"] )
            players.save()
        for i in range(20):
            bowl = BowlingLineUp( user_id = request.user, challenge_id = Challenges.objects.get(challenge_id =request.data["challenge_id"])  , player_id =request.data["overSelection"][i])
            bowl.save()
        
        

        return Response( status=status.HTTP_201_CREATED)

        

    @ensure_csrf_cookie
    @api_view([ 'POST','GET'])
    def challenge(request):
        if request.method=='POST':
            teamId = CricketTeam.objects.get(userId = request.user)
            teamId2 = CricketTeam.objects.get(id = request.data["challenged_team_id"]) 
            request.data["challenger_team_id"] = teamId.id
            request.data["user_name"] = request.user.name
            request.data["challenger_team_name"] = teamId.teamName
            request.data["challenged_team_name"] = teamId2.teamName
            request.data["user_id"] = request.user.id
            serializer = ChallengeSerializer(data=request.data,context={'request': request})  
            serializer.is_valid(raise_exception=True) 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            chall = CricketTeam.objects.get(userId = request.user)
            queryset= Challenges.objects.filter(challenger_team_id  = chall.id )
            queryset2= Challenges.objects.filter(challenged_team_id  = chall.id , is_accepted = True)
            serializer = ChallengeSerializer(list(queryset) +list( queryset2), many = True)
            # newdata = {
            #     'team_name' : chall.teamName,
            #     'user_name': request.user.name,
            #     'user_id' : request.user.id,
            #     'challenge' : serializer.data

                
            # }
            print(serializer.data,"get")
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return response.Response(UserSerializer(user).data)
    @api_view([ 'GET'])
    def incoming_challenges(request):
        print("users ", request.user)
        teamId = CricketTeam.objects.get(userId = request.user)
        queryset  = Challenges.objects.filter(challenged_team_id = teamId.id, is_accepted = False) 
        serializer = ChallengeSerializer(queryset, many = True)
         
        # if not serializer.is_valid():
        #     print (serializer.errors) 
        #     return response("incorrect serializer ", status = status.HTTP_404_NOT_FOUND)

        return Response(serializer.data,status=status.HTTP_200_OK)
        
    @ensure_csrf_cookie
    @api_view([ 'POST','GET'])
    def accept_challenges( request):
        print(request.data)
        queryset = Challenges.objects.get(challenge_id = request.data["challenge_Id"] )
        queryset.is_accepted = True
        queryset.save()
        print(queryset)
        serializer = ChallengeSerializer( queryset)
        #if not serializer.is_valid():
        #     print (serializer.errors) 
        #     return response("Faliure", status = status.HTTP_502_BAD_GATEWAY)
        # else:
        #serializer.update["is_accepeted"] = True
        #serializer.validated_data["is_accepeted"] = True
       # serializer.save()
        return Response("accepted", status=status.HTTP_200_OK)
