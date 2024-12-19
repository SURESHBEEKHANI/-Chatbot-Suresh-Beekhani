$(document).ready(function() {
  const chatContainer = $('.chat-container');
  const userInput = $('#user-input');
  const sendBtn = $('#send-btn');
  const messages = $('.messages');
  const typingIndicator = $('.typing-indicator');
  const errorMessage = $('.error-message');

  // Enable/disable send button based on input
  userInput.on('input', function() {
      sendBtn.prop('disabled', !this.value.trim());
  });

  // Handle message sending
  function sendMessage() {
      const message = userInput.val().trim();
      if (!message) return;

      // Add user message
      appendMessage(message, 'user-message');
      userInput.val('').trigger('input');

      // Show typing indicator
      typingIndicator.attr('aria-hidden', 'false');

      // Send to backend
      $.ajax({
          url: '/get',
          method: 'POST',
          data: { msg: message },
          success: function(response) {
              typingIndicator.attr('aria-hidden', 'true');
              appendMessage(response, 'bot-message');
          },
          error: function() {
              typingIndicator.attr('aria-hidden', 'true');
              showError();
          }
      });
  }

  // Append message to chat
  function appendMessage(text, className) {
      const messageDiv = $('<div>')
          .addClass(`message ${className}`)
          .append($('<p>').text(text));
      
      messages.append(messageDiv);
      scrollToBottom();
  }

  // Scroll chat to bottom
  function scrollToBottom() {
      const chatBox = $('.chat-box');
      chatBox.scrollTop(chatBox[0].scrollHeight);
  }

  // Show error message
  function showError() {
      errorMessage.attr('aria-hidden', 'false')
          .fadeIn()
          .delay(3000)
          .fadeOut(() => {
              errorMessage.attr('aria-hidden', 'true');
          });
  }

  // Event listeners
  sendBtn.on('click', sendMessage);
  userInput.on('keypress', function(e) {
      if (e.which === 13) sendMessage();
  });

  // Toggle chat
  $('.toggle-btn').on('click', function() {
      chatContainer.toggleClass('active');
      $(this).find('span').text(
          chatContainer.hasClass('active') ? '◀' : '▶'
      );
  });

  // Close chat
  $('.close-btn').on('click', function() {
      chatContainer.removeClass('active');
      $('.toggle-btn span').text('▶');
  });

  // Initial scroll
  scrollToBottom();
});

