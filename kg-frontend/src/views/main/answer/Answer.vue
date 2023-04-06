<template>
  <div>
    <div class="fileList"></div>
    <div class="chat" ref="chatContent">
      <div v-for="message in messages" :key="message.id">
        <div v-if="message.isMe" class="my-message">
          <img :src="require('assets/img/me.jpg')" class="avatar" />
          <div class="message-content">{{ message.content }}</div>
        </div>
        <div v-else class="other-message">
          <img :src="require('assets/img/other.jpeg')" class="avatar" />
          <div class="message-content message-content-right">{{ message.content }}</div>
        </div>
      </div>
    </div>
    <div class="input-box">
      <el-input
        v-model="newMessage"
        placeholder="请输入内容"
        class="input"
        @keyup.enter.native="sendMessage"
      ></el-input>
      <el-button type="primary" plain @click="sendMessage">发送</el-button>
    </div>
  </div>
</template>
<script>
export default {
  name: "Answer",
  components: {},
  data() {
    return {
      messages: [
        { id: 1, content: "你好", isMe: false },
        { id: 2, content: "你好啊", isMe: true },
        { id: 3, content: "最近怎么样？", isMe: false },
        { id: 4, content: "还不错，你呢？", isMe: true },
      ],
      newMessage: "",
    };
  },
  methods: {
    sendMessage() {
      if (this.newMessage) {
        this.messages.push({
          id: this.messages.length + 1,
          content: this.newMessage,
          isMe: true,
        });
        this.newMessage = "";
        this.$nextTick(() => {
          this.$refs.chatContent.scrollTop =
            this.$refs.chatContent.scrollHeight;
        });
        setTimeout(() => {
          this.messages.push({
            id: this.messages.length + 1,
            content: "回答内容",
            isMe: false,
          });
        }, 1000);
        setTimeout(() => {
          this.$nextTick(() => {
            this.$refs.chatContent.scrollTop =
              this.$refs.chatContent.scrollHeight;
          });
        }, 1000);
      }
    },
  },
};
</script>
<style scoped>
.fileList {
  width: 100%;
  height: 200px;
  border: 1px solid red;
  margin-top: 20px;
}
.chat {
  margin-top: 20px;
  width: 100%;
  height: 300px;
  border: 1px solid red;
  overflow-y: auto;
}
.my-message {
  display: flex;
  flex-direction: row-reverse;
  align-items: center;
  margin: 10px;
}

.other-message {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin: 10px;
}

.avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 10px;
}

.message-content {
  padding: 10px;
  border-radius: 10px;
  background-color: #eee;
  margin-right: 10px;
}
.input-box {
  display: flex;
  margin-top: 20px;
}

input {
  flex: 1;
  height: 30px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 0 10px;
}
</style>
