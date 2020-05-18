<template>
    <div class="single-question mt-2">
        <div class="container">
            <h1>{{question.content}}</h1>
            <QuestionActions
                    v-if="isQuestionAuthor"
                    :slug="question.slug"
            />
            <p class="mb-0">Posted by:
                <span class="author-name">{{question.author}} </span>
            </p>
            <p>{{question.created_at}}</p>
            <hr>
            <div v-if="userHasAnswered">
                <p class="answer-added">You have written an answer!</p>
            </div>
            <div v-else-if="showForm">
                <form class="form-card" @submit.prevent="onSubmit">
                    <div class="card-header px-3">
                        Answer the Question
                    </div>
                    <div class="card-block">
                        <textarea rows="5"
                                  v-model="newAnswerBody"
                                  class="form-control"
                                  placeholder="Write your Answer"
                        ></textarea>
                    </div>
                    <div class="card-footer px-3">
                        <button class="btn btn-sm btn-success" type="submit"> Submit Your Answer</button>
                    </div>
                </form>
                <p v-if="error" class="error mt-2">{{error}}</p>
            </div>
            <div v-else>
                <button class="btn btn-sm btn-success"
                        @click="showForm = true"
                >
                    Answer this question
                </button>
            </div>
            <hr>
        </div>
        <div class="container">
            <AnswerComponent v-for="answer in answers"
                             :answer="answer"
                             :requestUser="requestUser"
                             :key="answer.id"
                             @delete-answer="deleteAnswer"
            />
            <div class="my-4">
                <p v-show="loadingAnswers"> ...loading...</p>
                <button
                        v-show="next"
                        @click="getQuestionAnswers"
                        class="btn btn-sm btn-outline-success"
                >Load More
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    import {apiService} from "../common/api.service";
    import AnswerComponent from "../components/Answer.vue";
    import QuestionActions from "../components/QuestionActions";

    export default {
        name: "Question",
        props: { //define inputs of component
            slug: {
                type: String,
                required: true
            }
        },
        components: {
            QuestionActions,
            AnswerComponent
        },
        data() {
            return {
                question: {},
                answers: [],
                newAnswerBody: null,
                error: null,
                userHasAnswered: false,
                showForm: false,
                next: null,
                loadingAnswers: false,
                requestUser: null
            }
        },
        computed: {
            isQuestionAuthor() {
                return this.question.author === this.requestUser
            }
        },
        methods: {
            setPageTitle(title) {
                document.title = title
            },
            getQuestionData() {
                let endpoint = `/api/questions/${this.slug}/`;
                apiService(endpoint)
                    .then(data => {
                        this.question = data
                        this.userHasAnswered = data.user_has_answered
                        this.setPageTitle(data.content)
                    })
            },
            getQuestionAnswers() {
                let endpoint = `/api/questions/${this.slug}/answers/`;
                if (this.next) {
                    endpoint = this.next
                }
                this.loadingAnswers = true;
                apiService(endpoint).then(data => {
                    this.answers.push(...data.results)
                    this.loadingAnswers = false;
                    if (data.next) {
                        this.next = data.next;
                    } else {
                        this.next = null;
                    }
                })
            },
            onSubmit() {
                if (this.newAnswerBody) {
                    let endpoint = `/api/questions/${this.slug}/answer/`
                    apiService(endpoint, "POST", {body: this.newAnswerBody})
                        .then(data => {
                            this.answers.unshift(data)
                        })
                    this.newAnswerBody = null
                    this.showForm = false
                    this.userHasAnswered = true
                    if (this.error) {
                        this.error = null
                    }
                } else {
                    this.error = "Ypu can't send an empty answer!"
                }
            },
            setRequestUser() {
                this.requestUser = window.localStorage.getItem("username")
            },
            async deleteAnswer(answer) {
                let endpoint = `/api/answers/${answer.id}/`;
                try {
                    await apiService(endpoint, "DELETE");
                    this.$delete(this.answers, this.answers.indexOf(answer));
                    this.userHasAnswered = false;
                } catch (e) {
                    console.log(e)
                }
            }
        },
        created() {
            this.getQuestionData();
            this.getQuestionAnswers();
            this.setRequestUser();
        }
    }
</script>

<style scoped>
    .author-name {
        font-weight: bold;
        color: #DC3545;
    }

    .answer-added {
        font-weight: bold;
        color: green;
    }

    .error {
        font-weight: bold;
        color: red;
    }
</style>