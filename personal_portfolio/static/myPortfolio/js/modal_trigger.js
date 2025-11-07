document.addEventListener('DOMContentLoaded',function(){
    const modalEvent = document.getElementById("displaystatus");

    if(window.showThankYouModal){

        const myModal = new bootstrap.Modal(modalEvent)
        myModal.show()
    }
});