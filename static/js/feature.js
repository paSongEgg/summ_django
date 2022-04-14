/*전역 변수*/
var themes=['정치','경제','사회','생활','IT','세계'];
var clickedButton=localStorage.getItem("clicked");
window.onload=()=>{
    makeSectionButtons();
    makeLODbuttons();
    addEvent();
}
/*페이지 이동 버튼 조정하는 함수*/
function makeSectionButtons(){
    let container=document.getElementById("sectionButtons");
    let mainButton=document.createElement('button');
    let sections=['정치','경제','사회','생활/문화','IT/과학','세계'];
    mainButton.className="home_button_changeOption";
    mainButton.type="button";
    if(window.location.pathname.substring(0,2)!=='/s'){
        mainButton.innerText="주제별 뉴스";
    }
    else{
        mainButton.innerText="섹션 뉴스"
    }
    mainButton.addEventListener('click',(e)=>{
        let currentPath=window.location.pathname;
        console.log(currentPath.substring(0,2));
        if(currentPath.substring(0,2)==='/s'){
            currentPath='/';
        }
        else {
            currentPath='/sections';
        }
        window.location.href=currentPath;
    });
    container.appendChild(mainButton);
    for(var i=0;i<6;i++){
        let sectionButton=document.createElement('button');
        sectionButton.addEventListener('click',(e)=>sendSectionValue(e));
        sectionButton.value=themes[i];
        if(clickedButton===i)
            sectionButton.className="button_theme_clicked";
        else 
            sectionButton.className="button_theme";
        sectionButton.innerText=sections[i];
        sectionButton.type="button";
        container.appendChild(sectionButton);

    }
}

function sendSectionValue(e){
    let currentPath=window.location.pathname;
    let sectionValue=e.target.value;
    let i=0;
    for(i=0;i<6;i++){
        if(e.target.value===themes[i]) {
            localStorage.setItem("clicked",i);
            break;
        }
    }
    if(i===6)localStorage.removeItem("clicked");
    if(currentPath==='/') currentPath+='sections?';
    
    else if(currentPath==='/sections'){
        currentPath+='?';
    }
    else {
        currentPath+='&';
    }
    currentPath+='theme='+sectionValue;
    window.location.href=currentPath;
}

/*LOD 조정 버튼을 생성하는 함수*/

function makeLODbuttons(){
    let container=document.getElementById("lodButtons");
    let keywordButton=document.createElement('button');
    keywordButton.addEventListener('click',(e)=>sendLodValue(e));
    keywordButton.value='0';
    keywordButton.className="button_theme";
    keywordButton.innerText="키워드 보기";
    keywordButton.type="button";
    container.appendChild(keywordButton);
    for(var i=1;i<6;i++){
        let lodButton=document.createElement('button');
        lodButton.addEventListener('click',(e)=>sendLodValue(e));
        lodButton.value=i;
        lodButton.className="button_theme";
        lodButton.innerText=i;
        lodButton.type="button";
        container.appendChild(lodButton);
    }
}

function sendLodValue(e){
    let currentPath=window.location.pathname;
    let lodValue=e.target.value;
    if(currentPath==='/'||currentPath==='/sections'){
        currentPath+='?';
    }
    else {
        currentPath+='&';
    }
    currentPath+='number='+lodValue;
    window.location.href=currentPath;
}

function makeSortButton(){
    let container=document.getElementById("sortButtons");
    
    let button=document.getElementsByClassName("sort_button");
    for(var i=0;i<2;i++){
        let sortButton=document.createElement('button');
        sortButton.addEventListener('click',(e)=>changeSort(e));
        //sortButton.value=;
        sortButton.className="button_theme";
        sortButton.innerText=i;
        sortButton.type="button";
        container.appendChild(sortButton);
    }
}

function changeSort(e){
    let currentPath=window.location.pathname;
    let sortValue=e.target.value;
    if(currentPath==='/'||currentPath==='/sections'){
        currentPath+='?';
    }
    else {
        currentPath+='&';
    }
    currentPath+='sort='+sortValue;
    window.location.href=currentPath;
}