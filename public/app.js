const { createApp, ref, reactive, computed, onMounted } = Vue;

createApp({
  setup() {
    const provas = ref([]);
    const loading = ref(true);
    const error = ref(null);
    const currentRoute = ref('home');
    const toastMessage = ref('');
    let toastTimeout = null;

    const answers = reactive({
      prova_01: { 1: [], 2: [], 3: [], 4: [], 5: [] },
      prova_02: { 1: [], 2: [], 3: [], 4: [], 5: [] },
      prova_03: { 1: [], 2: [], 3: [], 4: [], 5: [] }
    });

    const submitted = reactive({
      prova_01: false,
      prova_02: false,
      prova_03: false
    });

    async function loadData() {
      loading.value = true;
      error.value = null;
      try {
        const res = await fetch('/provas.json');
        if (!res.ok) throw new Error(`Status ${res.status}`);
        const data = await res.json();
        provas.value = data.provas || [];
        initializeAnswers();
      } catch (err) {
        console.warn('Falha ao carregar /provas.json, tentando fallback /api/provas:', err);
        try {
          const resApi = await fetch('/api/provas');
          if (!resApi.ok) throw new Error(`Status API ${resApi.status}`);
          const dataApi = await resApi.json();
          provas.value = dataApi.provas || [];
          initializeAnswers();
        } catch (apiErr) {
          console.error('Falha em ambos endpoints:', apiErr);
          error.value = 'Falha ao carregar dados das avaliacoes. Recarregue a pagina.';
        }
      } finally {
        loading.value = false;
      }
    }

    function initializeAnswers() {
      provas.value.forEach(p => {
        if (!answers[p.id]) answers[p.id] = {};
        if (submitted[p.id] === undefined) submitted[p.id] = false;
        p.questoes.forEach(q => {
          if (!answers[p.id][q.numero]) answers[p.id][q.numero] = [];
        });
      });
    }

    const currentProva = computed(() => {
      if (currentRoute.value === 'home') return null;
      return provas.value.find(p => p.id === currentRoute.value) || null;
    });

    function getQuestionSum(provaId, qNum) {
      const list = answers[provaId]?.[qNum] || [];
      return list.reduce((acc, val) => acc + Number(val), 0);
    }

    function getQuestionSumFormatted(provaId, qNum) {
      const sum = getQuestionSum(provaId, qNum);
      return String(sum).padStart(2, '0');
    }

    function isQuestionCorrect(provaId, question) {
      const userSum = getQuestionSum(provaId, question.numero);
      return userSum === question.soma_correta;
    }

    const currentScore = computed(() => {
      if (!currentProva.value) return 0;
      const p = currentProva.value;
      return p.questoes.reduce((acc, q) => {
        return acc + (isQuestionCorrect(p.id, q) ? q.pontos : 0);
      }, 0);
    });

    const correctCount = computed(() => {
      if (!currentProva.value) return 0;
      const p = currentProva.value;
      return p.questoes.filter(q => isQuestionCorrect(p.id, q)).length;
    });

    const answeredCount = computed(() => {
      if (!currentProva.value) return 0;
      const p = currentProva.value;
      return p.questoes.filter(q => {
        const list = answers[p.id]?.[q.numero] || [];
        return list.length > 0;
      }).length;
    });

    function conferirGabarito(provaId) {
      submitted[provaId] = true;
      const scoreBar = document.getElementById('score-bar');
      if (scoreBar) {
        scoreBar.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
      showToast('Gabarito conferido. Veja o resultado e as justificativas detalhadas.');
    }

    function resetarProva(provaId) {
      if (answers[provaId]) {
        Object.keys(answers[provaId]).forEach(qNum => {
          answers[provaId][qNum] = [];
        });
      }
      submitted[provaId] = false;
      showToast('Respostas limpas com sucesso.');
    }

    function getPropositionDiagnostic(q, p, userChecked) {
      if (p.correto && userChecked) {
        return {
          type: 'success',
          label: 'Acerto: Item verdadeiro selecionado',
          cssClass: 'diag-success'
        };
      }
      if (!p.correto && !userChecked) {
        return {
          type: 'neutral',
          label: 'Acerto: Item falso nao selecionado',
          cssClass: 'diag-neutral'
        };
      }
      if (p.correto && !userChecked) {
        return {
          type: 'danger',
          label: 'Atencao: Item verdadeiro nao selecionado',
          cssClass: 'diag-danger'
        };
      }
      return {
        type: 'danger',
        label: 'Atencao: Item falso marcado indevidamente',
        cssClass: 'diag-danger'
      };
    }

    function detectRoute() {
      const path = window.location.pathname.toLowerCase();
      const params = new URLSearchParams(window.location.search);
      const provaParam = params.get('prova') || params.get('id');

      if (provaParam === 'prova_01' || provaParam === '1' || path.includes('/prova1')) {
        return 'prova_01';
      }
      if (provaParam === 'prova_02' || provaParam === '2' || path.includes('/prova2')) {
        return 'prova_02';
      }
      if (provaParam === 'prova_03' || provaParam === '3' || path.includes('/prova3')) {
        return 'prova_03';
      }
      return 'home';
    }

    function navigateTo(targetRoute) {
      currentRoute.value = targetRoute;
      let path = '/';
      if (targetRoute === 'prova_01') path = '/prova1';
      else if (targetRoute === 'prova_02') path = '/prova2';
      else if (targetRoute === 'prova_03') path = '/prova3';

      if (window.location.pathname !== path) {
        window.history.pushState({ route: targetRoute }, '', path);
      }
      updateDocumentTitle();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function updateDocumentTitle() {
      if (currentRoute.value === 'prova_01') {
        document.title = 'Simulado 01 - Gerencia de Configuracao';
      } else if (currentRoute.value === 'prova_02') {
        document.title = 'Simulado 02 - Gerencia de Configuracao';
      } else if (currentRoute.value === 'prova_03') {
        document.title = 'Simulado 03 - Gerencia de Configuracao';
      } else {
        document.title = 'Simulados de Estudos - Gerencia de Configuracao';
      }
    }

    function shareCurrentLink() {
      let path = '/';
      if (currentRoute.value === 'prova_01') path = '/prova1';
      else if (currentRoute.value === 'prova_02') path = '/prova2';
      else if (currentRoute.value === 'prova_03') path = '/prova3';

      const fullUrl = window.location.origin + path;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(fullUrl)
          .then(() => showToast('Link direto copiado: ' + fullUrl))
          .catch(() => showToast('Link direto: ' + fullUrl));
      } else {
        showToast('Link direto: ' + fullUrl);
      }
    }

    function showToast(msg) {
      toastMessage.value = msg;
      if (toastTimeout) clearTimeout(toastTimeout);
      toastTimeout = setTimeout(() => {
        toastMessage.value = '';
      }, 3500);
    }

    function scrollToQuestion(qNum) {
      const el = document.getElementById(`questao-${qNum}`);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    onMounted(() => {
      currentRoute.value = detectRoute();
      updateDocumentTitle();
      loadData();
      window.addEventListener('popstate', () => {
        currentRoute.value = detectRoute();
        updateDocumentTitle();
      });
    });

    return {
      provas,
      loading,
      error,
      currentRoute,
      currentProva,
      answers,
      submitted,
      currentScore,
      correctCount,
      answeredCount,
      toastMessage,
      getQuestionSum,
      getQuestionSumFormatted,
      isQuestionCorrect,
      conferirGabarito,
      resetarProva,
      getPropositionDiagnostic,
      navigateTo,
      shareCurrentLink,
      scrollToQuestion
    };
  }
}).mount('#app');
