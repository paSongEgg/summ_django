const sections = ["정치", "경제", "사회", "생활/문화", "IT/과학", "세계"];
const themes = ["정치", "경제", "사회", "생활", "IT", "세계"];
const buttonStyle = ["home-button-change-option", "button-theme"];
let container = document.getElementById("userInput");

const drawUserInput = () => {
  let searchParams = new URLSearchParams(location.search);
  let currentLodValue = searchParams.get("number");
  let user = `
    <span>뉴스를 읽기에 사용할 시간을 입력해주세요</span>
    <input id="userInputRange" type="number" min="5" max="30" value="30" onChange=showNews(event) style="width:3vw; margin-top: 1em;">
  `;
  if (currentLodValue == 4) container.insertAdjacentHTML("beforeend", user);
};
const buttonSet = () => {
  let searchParams = new URLSearchParams(location.search);
  let viewRange = document.getElementById("viewRange");
  let currentLodValue = searchParams.get("number");
  if (currentLodValue === "4") {
    let currentUserValue = searchParams.get("user");
    let userRange = document.getElementById("userInputRange");
    userRange.value = currentUserValue;
  }

  viewRange.value = currentLodValue;
  switch (viewRange.value) {
    case "1":
      console.log("one");
      document.getElementById("rangeValue").innerText =
        "LOD 레벨 1 : 키워드 | 예상 소요 시간 : 6분";
      break;
    case "2":
      document.getElementById("rangeValue").innerText =
        "LOD 레벨 2 : 통합 기사 10개 + 기사별 키워드 | 예상 소요 시간 : 12분";
      break;
    case "3":
      document.getElementById("rangeValue").innerText =
        "LOD 레벨 3 : 섹션별 3개 기사 + 섹션별 키워드(각 3개) | 예상 소요 시간 : 18분";
      break;
    default:
      document.getElementById("rangeValue").innerText =
        "LOD 레벨 4 : 사용자 입력 시간에 따른 기사 출력";
      break;
  }
};

const APPcontrol = () => {
  const setPage = () => {
    drawUserInput();
    buttonSet();
    addClickEvent();
  };
  const addClickEvent = function () {
    let sectionButton = document.getElementsByClassName("section-button");
    let sortButton = document.getElementsByClassName("news-table-click");

    Array.prototype.forEach.call(sortButton, function (button) {
      button.addEventListener("click", (e) => {
        let currentParam = new URLSearchParams(location.search);
        currentParam.set("sort", e.target.getAttribute("value"));
        window.location.href = `${
          window.location.pathname
        }?${currentParam.toString()}`;
      });
    });
  };
  return setPage();
};

const showNews = (event) => {
  let currentPath = window.location.pathname;
  var tmp = new URLSearchParams(location.search);
  tmp.set("user", event.target.value);
  window.location.href = currentPath + "?" + tmp.toString();
};
const rangeChange = (event) => {
  let currentPath = window.location.pathname;
  var tmp = new URLSearchParams(location.search);
  tmp.set("number", event.target.value);
  window.location.href = currentPath + "?" + tmp.toString();
};
APPcontrol();
