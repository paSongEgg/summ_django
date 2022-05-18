import drawButton from "./drawButton.js";

const APPcontrol = (function (drawBtn) {
  let setPage = function () {
    drawBtn.buttonDraw();
    drawBtn.buttonSet();
    addClickEvent();
  };
  const addClickEvent = function () {
    let sectionButton = document.getElementsByClassName("section-button");
    let sortButton = document.getElementsByClassName("news-table-click");

    document.getElementById("mainButton").addEventListener("click", (e) => {
      window.location.href = e.target.value;
    });
    /*수정할 것*/
    sectionButton.map((button) =>
      button.addEventListener("click", (e) => {
        let currenParam = new URLSearchParams(location.search);
        currenParam.set("theme", e.target.value);
        window.location.href = `${window.loction.pathname}?${
          currentParam / toString()
        }`;
      })
    );
    sortButton.map((button) =>
      button.addEventListener("click", (e) => {
        let currenParam = new URLSearchParams(location.search);
        currenParam.set("sort", direction);
        1;
        window.location.href = `${
          window.location.pathname
        }?${currenParam.toString()}`;
      })
    );
  };

  return {
    setPage: setPage,
  };
})(drawButton);

APPcontrol.setPage();
