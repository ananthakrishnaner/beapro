

const selected_profile = document.querySelector('.user-profile-list-section');
const user_profile = document.querySelector('.user-profile-section');
user_profile.onclick = () =>{
  setTimeout(() =>{
    selected_profile.style.display = "flex";
  },100);
  
};

