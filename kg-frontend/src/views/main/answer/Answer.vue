<template>
  <div>
    <div class="search">
      <el-input
        placeholder="请输入关键词"
        v-model="search"
        class="search_input"
        @keyup.enter.native="getSearchedFiles"
      >
        <i slot="prefix" class="el-input__icon el-icon-search"></i>
      </el-input>
    </div>
    <div class="fileList">
      <li
        v-for="(item, index) in fileList"
        :key="index"
        @click="getDocumentId(item.document_id)"
        class="file"
      >
        <span class="el-icon-document"></span>
        <span
          class="el-icon-check"
          v-show="isSelected(item.document_id)"
        ></span>
        <span>{{ item.title }}</span>
      </li>
    </div>
    <div class="block">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="params.currentpage"
        :page-size="params.pageSize"
        layout="prev, pager, next"
        :total="total"
      >
      </el-pagination>
    </div>
    <div class="chat" ref="chatContent">
      <div v-for="message in messages" :key="message.id">
        <div v-if="message.isMe" class="my-message">
          <img
            src="https://github.githubassets.com/favicons/favicon.svg"
            class="avatar"
          />

          <div class="message-content">{{ message.content }}</div>
        </div>
        <div v-else class="other-message">
          <!-- <img :src="require('assets/img/other.jpeg')" class="avatar" /> -->
          <img :src="require('assets/img/me.jpg')" class="avatar" />
          <div class="message-content message-content-right">
            {{ message.content }}
          </div>
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
      <el-button class="el-icon-s-promotion" plain @click="sendMessage"></el-button>
    </div>
    <!-- <div class="pair">问答对列表</div> -->
  </div>
</template>
<script>
import { getAnswer } from "api/answer";
import { getSuccessFiles, searchFile } from "api/file";
export default {
  name: "Answer",
  components: {},
  data() {
    return {
      total: 0,
      params: {
        //设置初始值
        currentpage: 1,
        pageSize: 5,
      },
      messages: [
        { id: 1, content: "你好", isMe: false },
        { id: 2, content: "你好啊", isMe: true },
        { id: 3, content: "最近怎么样？", isMe: false },
        { id: 4, content: "还不错，你呢？", isMe: true },
      ],
      newMessage: "",
      question: "",
      answer: "",
      fileList: [],
      document_id: -1,
      search: "",
      isSearch: false,
    };
  },
  methods: {
    getFiles() {
      this.isSearch = false;
    //   this.params={currentpage: 1,pageSize: 5}
      getSuccessFiles(this.params).then((res) => {
        this.fileList = res.data.data;
        this.total = res.data.total;
      });
    },
    handleSizeChange(val) {
      this.params.pageSize = val;
      if (this.isSearch) this.getSearchedFiles();
      else this.getFiles();
    },
    handleCurrentChange(val) {
      this.params.currentpage = val;
      if (this.isSearch) this.getSearchedFiles();
      else this.getFiles();
    },
    getDocumentId(document_id) {
      this.document_id = document_id;
    },
    isSelected(document_id) {
      return this.document_id == document_id;
    },
    async sendMessage() {
      if (this.document_id == -1) {
        this.$message({
          message: "请选择文件",
          type: "warning",
        });
      }
      if (!this.newMessage) {
        this.$message({
          message: "请输入内容",
          type: "warning",
        });
      }
      if (this.newMessage && this.document_id != -1) {
        this.messages.push({
          id: this.messages.length + 1,
          content: this.newMessage,
          isMe: true,
        });
        this.question = this.newMessage;
        this.newMessage = "";
        this.$nextTick(() => {
          this.$refs.chatContent.scrollTop =
            this.$refs.chatContent.scrollHeight;
        });
        this.answer = (
          await getAnswer({
            question: this.question,
            document_id: this.document_id,
          })
        ).data.answer;
        this.messages.push({
          id: this.messages.length + 1,
          content: this.answer,
          isMe: false,
        });
        this.$nextTick(() => {
          this.$refs.chatContent.scrollTop =
            this.$refs.chatContent.scrollHeight;
        });
        this.document_id = -1;
      }
    },
    getSearchedFiles() {
      this.isSearch = true;
    //   this.params={currentpage: 1,pageSize: 5}
      searchFile({
        title: this.search,
        currentPage: this.params.currentpage,
        pageSize: this.params.pageSize,
      }).then((res) => {
        this.fileList = res.data.data;
        this.total = res.data.total;
      },
      (err) => {
        console.log(err);
      });
    },
  },
  watch:{
    'isSearch':function(){
        this.params={currentpage: 1,pageSize: 5}
        if(this.isSearch) this.getSearchedFiles();
        else this.getFiles();
    }
  },
  created() {
    this.getFiles();
  },
};
</script>
<style scoped>
.search {
  width: 200px;
  margin-top: 20px;
  position: absolute;
  right: 100px;
  top: 80px;
}
.search:deep(.search_input) {
  width: 200px;
  height: 40px;
  line-height: 40px;
}
.el-icon-search {
  cursor: pointer;
}
.fileList {
  width: 70%;
  height: 180px;
  /* border: 1px solid red; */
  /* padding-top: 20px; */
  display: flex;
  position: relative;
}
.file {
  width: 120px;
  height: 140px;
  margin: 10px;
  margin-top: 0;
  cursor: pointer;
  text-align: center;
  position: relative;
}
.filelogo {
  width: 120px;
  height: 120px;
}
.el-icon-document {
  font-size: 120px;
}
.el-icon-check {
  font-size: 60px;
  position: absolute;
  bottom: -5px;
  right: 0;
  color: greenyellow;
  font-weight: 700;
}
.block {
  position: absolute;
  top: 220px;
  left: 32%;
}
.chat {
  padding-top: 20px;
  width: 80%;
  height: 380px;
  border: 1px solid #5e85bfed;
  border-radius: 20px;
  overflow-y: auto;
  border-bottom: none;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
  margin-left: 25px;
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
  margin-top: 0;
  width: 80%;
  margin-left: 24px;
  border-right: none;
}

input {
  flex: 1;
  height: 30px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 0 10px;
}
.pair {
  width: 100%;
  height: 200px;
  border: 1px solid red;
  margin-top: 20px;
}
</style>
