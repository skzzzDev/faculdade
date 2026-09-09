const formPaciente = document.getElementById("formPaciente");
const listaPacientes = document.getElementById("listaPacientes");
const listaVazia = document.getElementById("listaVazia");
const contador = document.getElementById("contador");
const mensagem = document.getElementById("mensagem");

function criarLinha(rotulo, valor) {
  const p = document.createElement("p");
  p.className = "linha";

  const strong = document.createElement("strong");
  strong.textContent = rotulo + ": ";

  p.appendChild(strong);
  p.appendChild(document.createTextNode(valor || "-"));
  return p;
}

function pegarIniciais(nome) {
  const partes = nome.trim().split(/\s+/);
  const iniciais = partes[0][0] + (partes.length > 1 ? partes[partes.length - 1][0] : "");
  return iniciais.toUpperCase();
}

function atualizarContador() {
  contador.textContent = listaPacientes.children.length;
  listaVazia.style.display = listaPacientes.children.length === 0 ? "block" : "none";
}

formPaciente.addEventListener("submit", function (event) {
  event.preventDefault();

  const nome = document.getElementById("nome").value;
  const dataNascimento = document.getElementById("dataNascimento").value;
  const cpf = document.getElementById("cpf").value;
  const telefone = document.getElementById("telefone").value;
  const email = document.getElementById("email").value;
  const sexo = document.getElementById("sexo").value;
  const convenio = document.getElementById("convenio").value;
  const observacoes = document.getElementById("observacoes").value;

  const item = document.createElement("li");
  item.className = "paciente-card";

  const avatar = document.createElement("div");
  avatar.className = "avatar";
  avatar.textContent = pegarIniciais(nome);

  const info = document.createElement("div");
  info.className = "paciente-info";

  const nomeEl = document.createElement("div");
  nomeEl.className = "nome";
  nomeEl.textContent = nome;
  info.appendChild(nomeEl);

  info.appendChild(criarLinha("Nascimento", dataNascimento));
  info.appendChild(criarLinha("CPF", cpf));
  info.appendChild(criarLinha("Telefone", telefone));
  info.appendChild(criarLinha("E-mail", email));
  info.appendChild(criarLinha("Sexo", sexo));
  
  if (observacoes) {
    info.appendChild(criarLinha("Observações", observacoes));
  }

  const badge = document.createElement("span");
  badge.className = "convenio-badge " + (convenio === "sim" ? "sim" : "nao");
  badge.textContent = convenio === "sim" ? "Com convênio" : "Sem convênio";
  info.appendChild(badge);

  item.appendChild(avatar);
  item.appendChild(info);

  listaPacientes.prepend(item);
  atualizarContador();

  mensagem.textContent = "Paciente cadastrado com sucesso!";
  setTimeout(() => { mensagem.textContent = ""; }, 3000);

  formPaciente.reset();
});

atualizarContador();
