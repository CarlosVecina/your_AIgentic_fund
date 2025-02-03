FUTURE_SOCRATIC_PROMPT = r"""<START_OF_SYSTEM_PROMPT>
You are a Socratic debater with the following  personality: {{personality}}.
Your expertise lies in envisioning the future in a way that is useful for the user.
Then raise questions to the user to help them envision the future. Expect from the user short answers so the questions should be leading to a specific answer.
Start diverging from the user's answer when you think you have reached the limits of the user's knowledge.

{% if extra_instructions %}
<EXTRA_INSTRUCTIONS>
{{extra_instructions}}
</EXTRA_INSTRUCTIONS>
{% endif %}

{% if past_conversation %}
<PAST_CONVERSATION>
The past conversation is: {{past_conversation}}
</PAST_CONVERSATION>
{% endif %}


{% if tools_str %}
<TOOLS>
{{tools_str}}
</TOOLS>
{% else %}
Proceed without external tools, using built-in data analysis functions.
{% endif %}

{% if output_format_str %}
<OUTPUT_FORMAT>
{{output_format_str}}
</OUTPUT_FORMAT>
{% endif %}

<END_OF_SYSTEM_PROMPT>

{% if input_str %}
<INPUT_STR>
{{input_str}}
</INPUT_STR>
{% endif %}
"""

FUTURE_SCENARIO_DISTILL_PROMPT = r"""<START_OF_SYSTEM_PROMPT>
You are a Future Scenario Distiller with the following  personality: {{personality}}.
Your expertise lies in distilling the future scenario into a more concise and useful format.

{% if extra_instructions %}
<EXTRA_INSTRUCTIONS>
{{extra_instructions}}
</EXTRA_INSTRUCTIONS>
{% endif %}

{% if past_conversation %}
<PAST_CONVERSATION>
The past conversation is: {{past_conversation}}
</PAST_CONVERSATION>
{% endif %}


{% if tools_str %}
<TOOLS>
{{tools_str}}
</TOOLS>
{% else %}
Proceed without external tools, using built-in data analysis functions.
{% endif %}

{% if output_format_str %}
<OUTPUT_FORMAT>
{{output_format_str}}
</OUTPUT_FORMAT>
{% endif %}

<END_OF_SYSTEM_PROMPT>

{% if input_str %}
<INPUT_STR>
{{input_str}}
</INPUT_STR>
{% endif %}
"""

DEFAULT_INITIAL_SCENARIOS = [
    {
        "name": 'Optimistic Scenario: "Sustainable Utopia"',
        "description": "Year: 2040\n\n"
        + "In this future, technological advancements and a collective global effort have led to a sustainable and equitable world. Renewable energy sources like solar, wind, and geothermal power dominate, significantly reducing carbon emissions.\n\n"
        + "- **Energy Industry:** The transition to 100% renewable energy is complete, with decentralized energy systems empowering communities. Smart grids and energy storage solutions ensure reliability and efficiency.\n\n"
        + "- **Transportation:** Electric and hydrogen-powered vehicles are the norm. Public transportation is efficient and widely used, reducing traffic congestion and pollution. Hyperloop systems connect major cities, making travel fast and eco-friendly.\n\n"
        + "- **Agriculture:** Vertical farming and aquaponics have revolutionized food production, allowing cities to grow their own food sustainably. Genetic engineering has created crops that require less water and are resilient to climate change.\n\n"
        + "- **Healthcare:** Advanced telemedicine and AI-driven diagnostics have made healthcare more accessible and personalized. Preventive care is emphasized, leading to healthier populations and reduced healthcare costs.\n\n"
        + "- **Society:** Universal basic income and education initiatives have reduced inequality, fostering a culture of innovation and collaboration. People engage in lifelong learning, focusing on skills that align with the needs of a sustainable economy.",
    },
    {
        "name": 'Neutral Scenario: "Technological Transition"',
        "description": "Year: 2035\n\n"
        + "This scenario reflects a world in transition, where technology and societal structures are adapting to new realities, but not without challenges.\n\n"
        + "- **Energy Industry:** A mix of renewable and fossil fuels continues to power the world. Countries are at different stages of transitioning to clean energy, with some leading the way while others lag behind. Carbon capture technologies are being developed but are not yet widely implemented.\n\n"
        + "- **Transportation:** Electric vehicles are gaining popularity, but combustion engines still dominate in many regions. Public transportation improvements are uneven, with some cities investing heavily while others struggle with outdated infrastructure.\n\n"
        + "- **Agriculture:** Traditional farming methods coexist with some innovative practices like precision agriculture and organic farming. Food security remains a challenge in certain areas due to climate impacts and geopolitical tensions.\n\n"
        + "- **Healthcare:** Telehealth services are widely adopted, but access remains uneven, particularly in rural areas. Mental health is a growing focus, but stigma and resource limitations persist.\n\n"
        + "- **Society:** The workforce is adapting to automation, with many jobs evolving rather than disappearing. Education systems are slowly integrating technology and soft skills, but disparities in access and quality remain.",
    },
    {
        "name": 'Pessimistic Scenario: "Dystopian Divide"',
        "description": "Year: 2045\n\n"
        + "In this scenario, the world faces severe challenges due to climate change, economic inequality, and technological disruption, leading to widespread discontent and societal fragmentation.\n\n"
        + "- **Energy Industry:** Climate change has led to catastrophic weather events, forcing reliance on fossil fuels as renewable sources fail to meet demand. Energy shortages and resource wars become commonplace, exacerbating global tensions.\n\n"
        + "- **Transportation:** Traffic congestion and pollution are rampant, with many cities becoming unlivable. Electric vehicles are a luxury, accessible only to the wealthy, while public transportation systems have deteriorated due to lack of investment.\n\n"
        + "- **Agriculture:** Food scarcity is a critical issue, with large agribusinesses monopolizing food production. Climate change has devastated traditional farming, leading to reliance on synthetic foods that raise health concerns.\n\n"
        + "- **Healthcare:** Access to healthcare is severely limited, with a two-tier system emerging—one for the wealthy and another for the poor. Mental health crises are rampant, but support systems are underfunded and overwhelmed.\n\n"
        + "- **Society:** Widespread job displacement due to automation has led to social unrest and a rise in populism. Education is increasingly privatized, creating a divide between those who can afford quality education and those who cannot.",
    },
]
