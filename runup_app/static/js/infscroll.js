// const csrf_token = document.querySelector("[name=csrfmiddlewaretoken]").value;

function setPageUrl(pg) {
    let nextpgUrl = new URL(document.URL);
    if (nextpgUrl.searchParams.has('page')){
        nextpgUrl.searchParams.set('page',pg);
    }else{
        nextpgUrl.searchParams.append('page',pg);
    }
    document.querySelector(".infinite-more-link").href = nextpgUrl.href;
}

if (document.querySelector(".infinite-more-link") != null) setPageUrl(2);

document.addEventListener("DOMContentLoaded", () => {
  let sentinel = document.querySelector("#sentinel");

  let observer = new IntersectionObserver((entries) => {
    // console.log(entries);
    let entry = entries[0];
    if (entry.intersectionRatio > 0) {
      //when scrolled down
      if (document.querySelector(".infinite-more-link") == null) return;
      next_pg_url = document.querySelector(".infinite-more-link").href;
      if (next_pg_url == document.URL) return;
      fetch(next_pg_url, {
        method: "POST",
        headers: {
          "content-Type": "application/json",
          "X-CSRFToken": csrf_token,
        },
        body:Text,
      })
      .then((response) => response.text())
      .then((data) => {
        let cl = document.querySelector(".infinite-container"); //containor link
        let dl = data.split('<token/>'); //data list ['상품 리스트 html','다음 페이지']
        cl.innerHTML += dl[0];
        next_link = dl[1].trim();
        if (next_link != '')
          setPageUrl(next_link);
        else document.querySelector(".infinite-more-link").href = '';
        
        let imageBox = document.querySelectorAll(".img_box");
        imageBox.forEach((item) => {
          item.addEventListener("touchstart", () => {
            // console.log("touchstart");
            const aFirstChildHref = item.firstChild.nextSibling.classList[2];
            const aSecondChildHref = item.firstChild.nextSibling.classList[1];
            isTouch = true;
            pressTimer = setInterval(() => {
              counter++;
              itemClickFunc(item, aFirstChildHref, aSecondChildHref);
            }, 500);
          });
        
          item.addEventListener("touchend", () => {
            // console.log("touchend");
            clearInterval(pressTimer);
            isTouch = false;
            counter = 0;
          });
        });
      })
      .catch((error) => {
        console.log(error);
      });
    }
  });
  observer.observe(sentinel);
});
