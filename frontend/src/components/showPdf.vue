<template>
  <div class="showPdf">
    <el-radio-group v-model="read_status" @change=update_read_status>
      <el-radio-button label="0">Unread</el-radio-button>
      <el-radio-button label="1">Roughly</el-radio-button>
      <el-radio-button label="2">Clearly</el-radio-button>
    </el-radio-group>

    <el-button @click="upPage">up</el-button>
    <el-button @click="downPage">down</el-button>
        <el-button @click="rotate += 90">&#x27F3;</el-button>
        <el-button @click="rotate -= 90">&#x27F2;</el-button>
        <el-button @click="$refs.pdf.print()">print</el-button>
        <el-button @click="exportFile">export</el-button>

        <div>
          <el-row :gutter="20">

            <el-col :span="17">
              <div v-if="loadedRatio > 0 && loadedRatio < 1"
                   style="background-color: green; color: white; text-align: center"
                   :style="{ width: loadedRatio * 100 + '%' }">
                {{ Math.floor(loadedRatio * 100) }}%
              </div>
              <pdf ref="pdf"
                   style="border: 1.8px liquid red"
                   :src="src"
                   :page="page"
                   :rotate="rotate"
                   @password="password"
                   @progress="loadedRatio = $event"
                   @error="error"
                   @numPages="numPages = $event">
              </pdf>
            </el-col>

            <el-col :span="7">
              <el-tabs type="border-card">
                <el-tab-pane label="Editer">
                  <textarea :value="content" @input="update" cols="44" rows="40"></textarea>
                  <br>
                  <el-button :value="submit" @click="submitNote">Submit note</el-button>
                </el-tab-pane>
                <el-tab-pane label="View">
                  <div v-html="compiledMarkdown"></div>
                </el-tab-pane>
              </el-tabs>
            </el-col>
          </el-row>
        </div>
  </div>
</template>
<script>

import pdf from 'vue-pdf'

export default {
    name: "showPdf",
    components: {
        pdf: pdf
    },
    data () {
        return {
            radio: "0",
            src:'https://arxiv.org/pdf/1604.02135.pdf',
            loadedRatio: 0,
            page: 1,
            numPages: 0,
            rotate: 0,
            note: [],
            content: "",
            read_status: 0,
        }
    },
    computed: {
        compiledMarkdown: function () {
            var marked = require('marked');
            return marked(this.input, { sanitize: true});
        }
    },
    methods: {
        password: function(updatePassword, reason) {
            updatePassword(prompt('password is "test"'));
        },
        error: function(err) {
            console.log(err);
        },
        update: function (e) {
            this.input = e.target.value;
        },
        exportFile: {},

        upPage () {
            if (this.page < this.numPages) {
                this.page = this.page + 1;
                this.content = this.note[this.page - 1].content;
            }
        },

        downPage () {
            if (this.page > 1) {
                this.page = this.page - 1;
                this.content = this.note[this.page - 1].content;
            }
        },
        submitNote () {
            var axios = require('axios');
            var qs = require('qs');
            axios.post('/api/save_note',
                       qs.stringify({ username: this.$route.params.name,
                                      hash_code: this.$route.params.hash_code,
                                      paper_page: this.$route.params.paper_page})
                      )
                .then((response) => {
                    if (response["error_num"] > 0)
                        console.log(response["msg"]);
                })
        },

        read_paper () {
            var axios = require('axios');
            var qs = require('qs');
            axios.post('/api/read_paper',
                       qs.stringify({ username: this.$route.params.name,
                                      hash_code: this.$route.params.hash_code })
                      )
                .then((response) => {
                    var gnote = response["note"];
                    gnote.sort(function(a, b) {
                        return (a["page"] - b["page"]);
                    });
                    this.note = gnote;
                    this.read_status = response["read_status"];
                });
        },
        update_read_status () {
            this.$http.get('/api/update_read_status?username='
                           + this.$route.params.name
                           + '&hash_code='
                           + this.$route.params.hash_code
                           + '&read_status='
                           + this.read_status)
                .then((response) => {
                    if (response["error_num"] > 0)
                        console.log(response["msg"]);
                })
        }

    },
    mounted: function() {
      //这个是钩子函数
      //如果cartView函数要执行，必须先执行钩子函数
      //这个钩子函数完成了对cratView函数的调用
      //应该注意的是，使用mounted 并不能保证钩子函数中
      // 的 this.$el 在 document 中。为此还应该引入
      // Vue.nextTick/vm.$nextTick
      this.$nextTick(function () {
          this.src = "http://127.0.0.1:8080/api/get_paper/?username="
              + this.$route.params.name
              + "&hash_code="
              + this.$route.params.hash_code;
          read_paper();
          content = note[0].content;
      })
    }
}
</script>

