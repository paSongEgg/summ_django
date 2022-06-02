const sections = ["정치", "경제", "사회", "생활/문화", "IT/과학", "세계"];
const themes = ["정치", "경제", "사회", "생활", "IT", "세계"];
const buttonStyle = ["home-button-change-option", "button-theme"];
let container = document.getElementById("sectionButtons");

const drawMainButton = () => {
  let mainButton =
    window.location.pathname === "/"
      ? `<button type='button' class=${buttonStyle[0]} id='mainButton' value='/sections'>주제별 뉴스</button>`
      : `<button type='button' class=${buttonStyle[0]} id='mainButton' value='/'>전체 뉴스</button>`;
  return mainButton;
};
const drawSectionButton = () => {
  let sectionButton = "";
  for (var i = 0; i < 6; i++)
    sectionButton += `
              <button 
                  type='button' 
                  class='${buttonStyle[1]}  section-button' 
                  value=${themes[i]} 
                  id=${themes[i]}
              >${sections[i]}
              </button>
          `;
  return sectionButton;
};
const buttonDraw = () => {
  container.insertAdjacentHTML("beforeend", drawSectionButton());
};
const buttonSet = () => {
  let searchParams = new URLSearchParams(location.search);
  let viewRange = document.getElementById("viewRange");
  let currentLodValue = searchParams.get("number");
  /*if (searchParams.get("theme") !== null) {
    document.getElementById(searchParams.get("theme")).className =
      "button-theme-clicked section-button";
  }*/
  viewRange.value = currentLodValue;
  console.log(viewRange.value);
  switch (viewRange.value) {
    case "1":
      console.log("one");
      document.getElementById("rangeValue").innerText =
        "LOD 레벨 1 : 키워드 | 예상 소요 시간 : 1분";
      break;
    case "2":
      document.getElementById("rangeValue").innerText =
        "LOD 레벨 2 : 통합 기사 10개 + 기사별 키워드 | 예상 소요 시간 : 10분";
      break;
    case "3":
      document.getElementById("rangeValue").innerText =
        "LOD 레벨 3 : 섹션별 3개 기사 + 섹션별 키워드(각 3개) | 예상 소요 시간 : 20분";
      break;
    default:
      document.getElementById("rangeValue").innerText =
        "LOD 레벨 4 : 섹션별 5개 기사 + 섹션별 키워드(각 5개) | 예상 소요 시간 : 30분";
      break;
  }
};

const APPcontrol = () => {
  const setPage = () => {
    //buttonDraw();
    buttonSet();
    //addClickEvent();
  };
  const addClickEvent = function () {
    let sectionButton = document.getElementsByClassName("section-button");
    let sortButton = document.getElementsByClassName("news-table-click");

    /*document.getElementById("mainButton").addEventListener("click", (e) => {
      window.location.href = e.target.value;
    });
    Array.prototype.forEach.call(sectionButton, function (button) {
      button.addEventListener("click", (e) => {
        let currentParam = new URLSearchParams(location.search);
        currentParam.set("theme", e.target.value);
        window.location.href =
          window.location.pathname === "/sections"
            ? `${window.location.pathname}?${currentParam.toString()}`
            : `/sections?${currentParam.toString()}`;
      });
    });*/
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

const rangeChange = (event) => {
  let currentPath = window.location.pathname;
  var tmp = new URLSearchParams(location.search);
  tmp.set("number", event.target.value);
  window.location.href = currentPath + "?" + tmp.toString();
};
APPcontrol();
