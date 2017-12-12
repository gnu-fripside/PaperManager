<template>
  <div class="showPdf">
    <el-radio-group v-model="read_status" @change=update_read_status>
      <el-radio-button label="0">Unread</el-radio-button>
      <el-radio-button label="1">Roughly</el-radio-button>
      <el-radio-button label="2">Clearly</el-radio-button>
    </el-radio-group >


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
                  <textarea :value="content" @input="changeContent" cols="44" rows="40"></textarea>
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
            src:"",
            loadedRatio: 0,
            page: 1,
            numPages: 0,
            rotate: 0,
            note: [ {
                page: 1,
                content: ""
            }],
            content: "",
            read_status: 0,
        }
    },
    computed: {
        compiledMarkdown: function () {
            var marked = require('marked');
            return marked(this.content, { sanitize: true});
        }
    },
    methods: {
        exportFile () {},

        password: function(updatePassword, reason) {
            updatePassword(prompt('password is "test"'));
        },
        error: function(err) {
            console.log(err);
        },
        changeContent: function (e) {
            this.content = e.target.value;
        },

        upPage () {
            if (this.page < this.numPages) {
                this.page = this.page + 1;
                this.content = this.note[this.page].content;
            }
        },

        downPage () {
            if (this.page > 1) {
                this.page = this.page - 1;
                this.content = this.note[this.page].content;
            }
        },
        submitNote () {
            var axios = require('axios');
            var qs = require('qs');
            axios.post('/api/save_note',
                       qs.stringify({ username: this.$route.params.name,
                                      hash_code: this.$route.params.hash_code,
                                      paper_page: this.page,
                                      content: this.content})
                      )
                .then((response) => {
                    if (response.data["error_num"] > 0) {
                        console.log(response["msg"]);
                    } else {
                        this.note[this.page].content = this.content;
                    }
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
                    var gnote = response.data["note"];
                    gnote.sort(function(a, b) {
                       return (a["page"] - b["page"]);
                    });
                    this.note = gnote;
                    this.content = gnote[1].content;
                    this.read_status = response["read_status"];
                   
                });
        },

        initia () {
            this.read_paper();
            console.log(this.note);
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
                });
        }

    },
    mounted: function() {
        this.$nextTick(function () {
          this.src = ( "http://127.0.0.1:8080/api/get_paper?username="
                       + this.$route.params.name
                       + "&hash_code="
                       + this.$route.params.hash_code);
            this.initia();
      })
    }
}
</script>

