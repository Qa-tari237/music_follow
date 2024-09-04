var videos = [
    { id: 1, title: "Video 1", url: "path_to_video_1.mp4" },
    { id: 2, title: "Video 2", url: "path_to_video_2.mp4" },
    { id: 3, title: "Video 3", url: "path_to_video_3.mp4" }
    // Add more video objects as needed
  ];
  
  videos.forEach(function(video) {
    var videoItem = document.createElement("div");
    videoItem.className = "video-item";
    
    var videoElement = document.createElement("video");
    videoElement.src = video.url;
    videoElement.controls = true;
    
    var titleElement = document.createElement("p");
    titleElement.textContent = video.title;
    
    videoItem.appendChild(videoElement);
    videoItem.appendChild(titleElement);
    
    document.querySelector(".video-container").appendChild(videoItem);
  });


  document.getElementById('toggle-link').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent the default link behavior

    var toggleList = document.getElementById('toggle-list');
    
    if (toggleList.classList.contains('hidden')) {
        toggleList.classList.remove('hidden');
        this.textContent = 'Reduce';
    } else {
        toggleList.classList.add('hidden');
        this.textContent = 'Profile';
    }
});

document.getElementById('fileInput').addEventListener('change', function(event) {
  const file = event.target.files[0];
  if (file) {
      const reader = new FileReader();
      reader.onload = function(e) {
          document.getElementById('profilePic').src = e.target.result;
      };
      reader.readAsDataURL(file);
  }
});

document.getElementById('sendButton').addEventListener('click', function() {
  const messageInput = document.getElementById('messageInput');
  const messageText = messageInput.value.trim();
  if (messageText !== '') {
      const chatMessages = document.getElementById('chatMessages');
      
      const messageDiv = document.createElement('div');
      messageDiv.classList.add('message');

      messageDiv.innerHTML = `
          <div class="message-avatar">
              <img src="avatar1.png" alt="User">
          </div>
          <div class="message-content">
              <span class="message-user">You</span>
              <p>${messageText}</p>
              <span class="message-time">${new Date().toLocaleTimeString([], {hour: '2-digit', minute: '2-digit'})}</span>
          </div>
      `;

      chatMessages.appendChild(messageDiv);
      messageInput.value = '';
      chatMessages.scrollTop = chatMessages.scrollHeight;
  }
});

function uploadImage() {
    var name = document.getElementById('name').value;
    var fileInput = document.getElementById('profile-picture');
    var file = fileInput.files[0];
    var formData = new FormData();

    formData.append('name', name);
    formData.append('profile_picture', file);

    fetch('/upload/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
        } else if (data.error) {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to upload image');
    });
}