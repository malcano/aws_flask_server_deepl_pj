import collections

class getFlower:
    """
    sentiment code
    불안    0
    분노    1
    상처    2
    슬픔    3
    기쁨    4

    circumstance code
    대인관계    0
    진로, 취업, 직장    1
    연애, 결혼, 출산    2
    가족관계 3
    학업 및 진로    4
    학교폭력 따돌림    5
    재정, 은퇴,노후준비    6
    직장, 업무스트레스    7
    건강죽음    8
    """
    def __init__(self):
        sentiment_nervous = [# 불안
            {"국화 'AZMA'": "평화, 지혜", "프리지아 'Yellow'":"새로운 시작을 응원합니다, 천진난만, 익살스러움"},# 대인관계
            {"영춘화 'Winter Jasmine'": "희망, 기다림, 겨울이 끝나고 봄이 오기를 기다림", "리시안셔스 'ARENA GREEN'":"변치않는 사랑, 신뢰, 나를 믿어줘"},#진로
            {"스토크 'LIGHT PUPLE'":"참된 사랑, 진실하고 깊은 사랑, 영원한 사랑","등골나무 'Eupatorium chinensis Linne'":"주저, 망설임"},#연애
            {"천일홍 'Gomphrena Globosa'":"불변, 변치 않는 사랑", "수국 'GREEN'":"한결 같은 사랑, 희망, 청춘의 맹세"},#가족
            {"남천 'Nandina'":"전화위복","국화 'FORD'":"밝은 마음"},#학업
            {"보리사초 'BORI'":"단결, 협동","아스틸베 'ASTILBE'":"기약없는 사랑, 나는 여전히 당신을 기다립니다"},#학폭
            {"설유화_잎 'BRIDAL WREATH'":"선언, 노력, 단정한 사랑","안스리움 'TROPICAL'":"번뇌, 불타는 마음, 사랑에 번민하는 마음"},#재정
            {"안개 'BABY'S BREATH'":"맑은 마음, 사랑의 성공","국화 'POMPON MUM'":"정말 좋은 친구, 서로를 사랑하고 아끼는 마음, 진실"},#직장
            {"유스가스 'RUSCUS'":"변치않는 소중함","마트리카리아 'SUNNY-SIDE-UP'":"역경에 굴하지 않는 강인함"} #건강
        ]
        sentiment_annoy = [# 분노
            {"아네모네 'Windflower'": "고독, 배신, 사랑의 괴로움", "국화 'LAX'":"평화, 지혜"},# 대인관계
            {"엽란 'ASPIDISTRA'": "인내력과 끈기, 끊임없는 성장, 거절","리시안셔스 'ARENA GREEN'":"변치않는 사랑, 신뢰, 나를 믿어줘"},#진로
            {"수국 'Antique Green'":"변덕, 고집, 인내심이 강한 사랑","스토크 'WHITE'":"순결, 참된 사랑, 신념"},#연애
            {"장미 'JANA'":"우아한 사랑, 지속적이고 튼튼한 사랑, 사랑의 대상","유스가스 'RUSCUS'":"변치않는 소중함"},#가족
            {"유칼립투스 'PABLO'":"집중력, 상쾌함, 정신 집중","장미 'Ileos'":"불가침, 완벽한 성취"},#학업
            {"델피니움 'Delphinium'":"당신은 왜 나를 싫어합니까, 제 마음을 헤아려주세요, 자유롭게 살아가는 인생","옥시 'BLUE STAR'":"믿는 마음, 희망의 빛, 어려운 시기에 우리를 격려하고 위로하는데 도움"},#학폭
            {"기린초 'ORANGE STONECROP'":"근면성실, 노력하는 모습, 일상적인 노력과 인내심", "유칼립투스 'BLACKJACK'":"추억, 행운"},#재정
            {"마트리카리아 'SUNNY-SIDE-UP'":"역경에 굴하지 않는 강인함, 행복한 기억, 인내","스토크 'Apricot'":"믿어주세요, 절제된 사랑"},#직장
            {"백공작초 'WHITE HEATH ASTER'":"인내, 희망, 기다림", "유채 'Canola'":"명랑, 쾌활, 새로운 시작과 변화"}] #건강
        sentiment_hurt =[# 상처
            [{"국화 'Peach PangPang'": "당신을 사랑해요, 사랑과 감사, 순결한 마음"},
            {"작약 'SARA'":"청초한 사랑, 정이 깊어 떠나지 못한다, 작약지중"}],# 대인관계
            [{"마트리카리아 'SUNNY-SIDE-UP'": "역경에 굴하지 않는 강인함, 인내"},
             {"아카시아 'Acacia'":"친교, 깨끗한 마음, 우정, 숨겨진 사랑"}],#진로
            [{"안스리움 'Japira''":"번뇌, 불타는 마음, 사랑의 고뇌"},
             {"장미 'ALL4LOVE'":"사랑을 위해, 모든 것을 다 줄께, 진실된 사랑"}],#연애
            [{"튤립 'Stronggold'":"용기와 결심, 새로운 시작, 긍정적인 마인드와 자신감"},
             {"쿠루쿠마 'CURUCUMA'":"당신을 사랑합니다, 우정, 위로"}],#가족
            [{"과꽃 'MINI CALLISTEPHUS'":"믿는 마음, 보상, 인내"},
             {"백합 'YELLOWWIN'":"금전운, 자신감"}],#학업
            [{"스토크 'Pink'":"믿어주세요, 영원한 사랑"},
             {"옥시 'BLUE STAR'":"믿는 마음, 희망의 빛, 어려운 시기에 우리를 격려하고 위로하는데 도움"}],#학폭
            [{"라넌큘러스 하노이 'Ranunculus Hanoi'":"비난하다, 망은(忘恩), 은혜를 잊는 것"},
             {"장미 'Revival'":"온화함, 다정함, 나의 마음 그대만이 아네"}],#재정
            [{"라넌큘러스 아리아드네 'Ranunculus Ariadne'":"용기와 인내력, 어려운 시기에도 굳건한 신념과 결의를 가지고 인내"},
             {"심포리 카르포스 'RedBerry'":"친절, 현명, 열정적인 사랑"}],#직장
            [{"메리골드, 'MARIGOLD'":"반드시 오고야 말 행복, 빛나는 미래, 행운"},
             {"튤립 'Dynasty'":"사랑의 시작, 애정, 배려"}]] #건강
        sentiment_sad =[# 슬픔
            [{"안스리움 'Japira'": "번뇌, 사랑에 번민하는 마음, 사랑의 고뇌"},
            {"장미 'Aqua'":"기적, 포기하지 않는 사랑, 순수하고 청초한 마음"}],# 대인관계
            [{"아미초 'LACE'": "끈기, 인내, 기다림"},
             {"스토크 'Apricot'":"믿어주세요, 절제된 사랑, 행복한 사랑"}],#진로
            [{"파니쿰 'PENICUM'":"애수, 마음을 서글프게 하는 슬픈 시름"},
             {"국화 'Peach PangPang'":"당신을 사랑해요, 사랑과 감사, 순결한 마음"}],#연애
            [{"튤립 'Stronggold'":"용기와 결심, 새로운 시작, 희망"},
             {"금어초 'Snapdragon'":"수다쟁이, 주제넘게 참견하다, 남몰래 물고기를 잡다"}],#가족
            [{"과꽃 'MINI CALLISTEPHUS'":"믿는 마음, 인내, 믿음직한 사랑"},
             {"리시안셔스 'ARENA GREEN'":"변치않는 사랑, 신뢰, 나를 믿어줘"}],#학업
            [{"델피니움 'Delphinium'":"당신은 왜 나를 싫어합니까, 제 마음을 헤아려주세요, 자유롭게 살아가는 인생"},
             {"국화 'DIAMOND'":"순결한 사랑, 사랑의 강인함과 영원, 순수하고 강한 마음"}],#학폭
            [{"마트리카리아 'SUNNY-SIDE-UP'":"역경에 굴하지 않는 강인함, 인내, 관용"},
             {"옥시 'BLUE STAR'":"믿는 마음, 희망의 빛, 어려운 시기에 우리를 격려하고 위로하는데 도움"}],#재정
            [{"리시안셔스 보라복겹 'Prairie Gentian'":"희망과 감사, 어려움을 극복, 긍정적인 에너지"},
             {"아스그레피아스 'TUBEROSA'":"화려한 추억, 정열적인 사랑"}],#직장
            [{"디디스커스 'Didiscus'":"영원한 아름다움, 강한 생명력, 사랑하는 사람에 대한 그리움"},
             {"라넌큘러스 아리아드네 'Ranunculus Ariadne'":"변하지 않는 사랑, 용기와 인내력, 어려운 시기에도 굳건한 신념과 결의를 가지고 인내"}]]#건강
        sentiment_joy =[# 기쁨
            [{"솔리다스터 'Solidago'": "축복, 강한 결실, 자신감"},
            {"심포리 카르포스 'RedBerry'":"친절, 현명, 열정적인 사랑"}],# 대인관계
            [{"프리지아 'White'": "새로운 시작을 응원합니다, 순수함, 새로운 우정"},
             {"헬리옵시스 'Heliopsis'":"추억, 쾌활한 마음, 긍정적인 에너지"}],#진로
            [{"스토크 'WHITE'":"순결, 신념, 영원한 사랑"},
             {"냉이초 'PETTY COAT' ":"당신에게 모든것을 드릴게요, 우아함, 귀족적인 아름다움"}],#연애
            [{"골든볼 'GOLDEN BALL'":"끝없는 사랑, 이상적인 사랑, 행복한 가정"},
             {"수국 'SNOW BALL'":"행복한 가정, 가정의 안정과 사랑"}],#가족
            [{"카라 'CAPTAIN ROMANCE'":"순수, 열정, 존경과 감사의 마음"},
             {"스토크 'Stock'":"결실, 보랏빛의 기다림, 정열적인 사랑의 상징"}],#학업
            [{"알스트메리아 'ALSTROEMERIA'":"새로운 만남, 배려, 우정"},
             {"쿠루쿠마 'CURUCUMA'":"당신을 사랑합니다, 우정, 위로"}],#학폭
            [{"장미 'VICTORIA' ":"승리, 성공, 축하와 응원"},
             {"해바라기 'VINCENT'":"풍요와 부귀를 상징함"}],#재정
            [{"백합 'YELLOWWIN'":"행복, 금전운, 자신감"},
             {"다알리아 'DAHLIA' ":"정열, 고귀함, 당신을 알아 기쁩니다"}],#직장
            [{"불노초 'FOREVER YOUNG'":"영원한 청춘, 영원한 젊음"},
             {"다알리아 'ORANGE POMPON DAHLIA' ":"감사, 우아, 인내"}]] #건강

        self.flowerList = [sentiment_nervous, sentiment_annoy, sentiment_hurt, sentiment_sad, sentiment_joy]

    def fromFlowerList(self, sentiment: int, circumstance: int):
        """
        :param sentiment: sentiment code
        :param circumstance: circumstance code
        :return: list[{'flower name1':'sentence'},{'flower name2':'sentence'}]
        """
        return self.flowerList[sentiment][circumstance]

    def imglink(self, sentiment: int, circumstance: int):
        """
        :param sentiment:
        :param circumstance:
        :return:
        """
    def getSentiment(self, sentiment_number):
        if sentiment_number == 0:
          return '불안'
        elif sentiment_number == 1:
          return '분노'
        elif sentiment_number == 2:
          return '상처'
        elif sentiment_number == 3:
          return '슬픔'
        elif sentiment_number == 4:
          return '기쁨'
    def getCircumstance(self, circumstance_number):
        if circumstance_number == 0:
          return '대인관계'
        elif circumstance_number == 1:
          return '진로,취업,직장'
        elif circumstance_number == 2:
          return '연애,결혼,출산'
        elif circumstance_number == 3:
          return '가족관계'
        elif circumstance_number == 4:
          return '학업 및 진로'
        elif circumstance_number == 5:
          return '학교폭력/따돌림'
        elif circumstance_number == 6:
          return '재정,은퇴,노후준비'
        elif circumstance_number == 7:
          return '직장, 업무 스트레스'
        elif circumstance_number == 8:
          return '건강,죽음'