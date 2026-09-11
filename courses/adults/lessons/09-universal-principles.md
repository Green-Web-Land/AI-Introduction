# Universal Principles for AI

[Home](../README.md) · [Curriculum](../CURRICULUM.md)

Lesson AIE-09 · Foundation chapter · Draft · 2026-09-11

**Your goal:** turn a proposed principle into a practical responsibility and a check you can perform.

> AI should expand human capability while preserving human choice, responsibility and the ability to question it.

These are **our proposed principles for developers, providers and users**. “Universal” describes our intended breadth: we want these questions considered wherever AI is used. It does not mean one worldwide rulebook exists, that every system follows these principles, or that this course creates enforceable rights.

You do not need an AI account for this lesson. All examples are fictional.

## Four things that must not be confused

| Kind | What it does | Example | What to check |
|---|---|---|---|
| Principle | States a value or direction for decisions. | “Respect privacy.” | What specific behaviour would put this into practice? |
| Enforceable law | Establishes legal requirements within its applicable scope. | A requirement affecting how an organisation handles personal information. | Which jurisdiction, activity and current rule apply? Seek qualified advice when necessary. |
| Product policy | States a provider's or organisation's rules and commitments. | A service's published data-use policy or workplace rule for approved tools. | Which policy and version apply, and what exceptions or settings matter? |
| Technical safeguard | Implements a restriction, protection or detection mechanism. | An integration that can read selected files but cannot send email. | Is the control configured, effective and tested within the authorised environment? |

These categories can interact. A law can require a control; a policy can implement a principle. They are not interchangeable. A product policy may have contractual consequences, but it is not automatically legislation. This lesson does not determine which laws apply to a particular service or person.

**Writing “respect privacy” in a prompt does not itself protect private data.** For example, first remove unnecessary personal details, use an authorised service, check its data handling and limit access. A prompt can communicate a boundary, but it cannot replace the controls needed to enforce it.

## Eleven proposed principles

### 1. Human dignity and agency

Help people understand and choose. Do not deceive, coerce or exploit their vulnerabilities.

**Everyday example:** an assistant explains several study options and lets the learner choose. **Failure example:** it pressures the learner to buy a service by claiming they cannot succeed alone. **Practical check:** can the person decline, ask questions and choose an alternative without manipulation?

### 2. Safety and proportionality

Match the checks to the possible harm. A draft shopping list and an action affecting someone's livelihood need different levels of scrutiny.

**Everyday example:** review a meeting invitation before sending it. **Failure example:** use an unverified recommendation to make a consequential decision. **Practical check:** what could go wrong, who could be affected, and does the proposed review address that risk? Human review is useful only when the reviewer has enough information and authority to intervene.

### 3. Honesty and uncertainty

Distinguish supplied facts, assumptions, estimates and invented examples. Do not fabricate evidence or hide uncertainty.

**Everyday example:** a summary marks a missing date as unknown. **Failure example:** it invents a source to make a claim look reliable. **Practical check:** can you trace important claims to evidence, and do those sources actually support them?

### 4. Privacy and consent

Use only necessary information with appropriate authority and permission. Explain relevant uses and protect sensitive information.

**Everyday example:** use a synthetic customer record to demonstrate a problem. **Failure example:** upload the entire customer database for a small formatting task. **Practical check:** what information is necessary, who may receive it, and what permits that use? A person's willingness to share does not automatically settle every privacy obligation.

### 5. Limited authority

Give AI only the access needed for the agreed task. Permission to advise is not permission to act.

**Everyday example:** allow access to one selected document to prepare a summary. **Failure example:** connect the whole account and allow sending or deletion when only drafting was requested. **Practical check:** inspect actual permissions, permitted actions and the point where further approval is needed.

### 6. Accountability

Identify who is responsible for decisions, corrections and consequences. “The AI did it” does not end that responsibility.

**Everyday example:** a named editor checks a published guide and receives correction reports. **Failure example:** the provider and operator each send the affected person to the other without a clear owner. **Practical check:** who can explain the decision, correct the result and follow through? Keep only the records needed for that purpose, with appropriate protection.

### 7. Fairness and accessibility

Consider who benefits, who may be harmed and who cannot use the technology. Test assumptions about language, ability, resources and experience.

**Everyday example:** provide a readable text lesson as well as an optional video. **Failure example:** make a paid AI account the only way to understand essential instructions. **Practical check:** ask people with different needs to identify barriers; provide a workable alternative where needed.

### 8. Verification and challenge

Make important results checkable. Give affected people a meaningful way to question them and seek appropriate human review.

**Everyday example:** show the supplied figures behind a calculated total. **Failure example:** reject a correction because the system sounds certain. **Practical check:** can a reviewer examine the relevant evidence and change an incorrect outcome? A fluent explanation is not proof of correctness.

### 9. Control and recovery

Provide ways to stop actions, correct mistakes and recover where possible. Explain actions that cannot reliably be undone before taking them.

**Everyday example:** show a proposed document change before applying it and retain an appropriate recoverable version. **Failure example:** send confidential material and assume deleting the sent message retrieves every copy. **Practical check:** what does Stop prevent, what has already happened, and what recovery has actually been verified?

### 10. Human growth

Strengthen understanding and independent skills. Judge success by useful outcomes, not dependence or time spent using AI.

**Everyday example:** a learner attempts a problem, receives a hint and then explains their answer unaided. **Failure example:** completed answers accumulate while the learner cannot explain the work. **Practical check:** can the person perform a comparable task or explain the result without assistance?

### 11. Responsible improvement

Use evaluated feedback to improve usefulness and reliability without treating people's private information as freely available material.

**Everyday example:** report a reproducible failure using fictional data. **Failure example:** collect sensitive conversations “to improve AI” without resolving permission or data handling. **Practical check:** what feedback is necessary, where will it go, and how will improvement be assessed? Correcting one answer does not establish that a model has been permanently retrained. See [Prediction: feedback and improvement](08-prediction.md).

## Who puts the principles into practice?

| Responsibility | Practical contribution |
|---|---|
| Developers | Design permissions, failure handling, accessible interfaces and checks that can be tested. |
| Providers and organisations deploying AI | Explain relevant capabilities and data practices, configure controls, define accountable owners and respond to problems. |
| Users | Choose suitable tasks, protect information, stay within their authority and check important outputs. |
| People affected by AI use | Should have understandable information and a meaningful route to raise concerns under these proposed principles. They do not need to be customers to matter. |

Responsibilities can overlap. Users should not have to compensate for every hidden design problem, and developers cannot anticipate every use without feedback. The practical question is who can prevent or remedy this particular problem.

## When principles pull in different directions

Keeping a record may help accountability while retaining unnecessary personal details harms privacy. Adding approvals may reduce risk while making a simple task harder to access.

Use this approach: identify the affected people and possible harms; establish applicable requirements; consider less intrusive alternatives; select proportionate controls; name the responsible decision-maker; and check the outcome. A trade-off is not permission to ignore applicable obligations or conceal the impact.

## Exercise: review a proposed assistant

A fictional community group wants AI to draft replies to enquiries. Its proposal says: “The AI will respect privacy. Connect the shared mailbox, let it send replies automatically and keep all messages indefinitely so it can learn. A volunteer can check occasionally.”

Identify at least four weaknesses. For each, write one principle, one concrete remedy and one check. Then explain why the sentence about privacy is insufficient.

**Answer guidance:**

- Limited authority: start with drafting from selected, necessary information; verify sending is disabled in actual permissions.
- Privacy: define permitted data, recipients and retention; check the service's relevant practices before supplying records. Do not assume indefinite retention is necessary or that messages train the model.
- Accountability and verification: name a responsible reviewer and a workable review process; check that incorrect drafts can be corrected before they reach people.
- Control and recovery: explain what can be stopped or recovered; do not promise that sent messages can always be recalled.

Other sound answers may address accessibility, honesty or the group's capacity to review. The privacy sentence expresses intent; it does not show that permissions, storage or disclosure are controlled.

You pass this exercise when your remedies are specific enough to check and you distinguish a written aspiration from an implemented control. This is a design exercise, not permission to connect or test a real mailbox.

## Apply one principle today

Choose a small AI task. Write: **Who is affected? What is permitted? Who checks the result? What happens if it is wrong?** If you cannot answer, narrow the task or resolve the missing information before proceeding.
