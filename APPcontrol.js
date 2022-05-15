import drawButton from "./drawButton.js";
const APPcontrol = ((drawBtn) => {
  const setPage = () => {
    drawBtn.draw();
    drawBtn.set();
  };
  const addButtonClickEvent = () => {
    let sectionButton = document.getElementsByClassName("section-button");
    document.getElementById("mainButton").addEventListener("click", (e) => {
      window.location.href = e.target.value;
    });
    /*수정할 것*/
    sectionButton.map((button) =>
      button.addEventListener("click", (e) => {
        window.location.href = e.target.value;
      })
    );
  };
  return {
    init() {
      setPage();
    },
  };
})(drawButton);

APPcontrol.init();
