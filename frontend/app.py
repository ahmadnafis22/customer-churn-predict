
import requests
import streamlit as st


# ==================================================
# 1. Page Configuration
# ==================================================
st.set_page_config(
    page_title="Telco Churn AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==================================================
# 2. Custom Styling
# ==================================================

# ==================================================
# Custom Styling - Telco Churn AI
# ==================================================
st.markdown(
    """
    <style>
    /* Main application */
    .stApp {
        background:
            radial-gradient(
                ellipse at 5% 0%,
                rgba(37, 99, 235, 0.13),
                transparent 38%
            ),
            #080d19;
        color: #e2e8f0;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2.2rem;
        padding-bottom: 3rem;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #0c1424;
        border-right: 1px solid #1e293b;
    }

    [data-testid="stSidebar"] h1 {
        color: #93c5fd;
        font-size: 1.5rem;
    }

    /* Hero section */
    .hero {
        position: relative;
        overflow: hidden;
        padding: 38px 36px;
        border-radius: 24px;
        background: linear-gradient(
            125deg,
            #142850 0%,
            #101c35 55%,
            #102a43 100%
        );
        border: 1px solid rgba(96, 165, 250, 0.24);
        box-shadow: 0 18px 50px rgba(0, 0, 0, 0.22);
        margin-bottom: 28px;
    }

    .hero-tag {
        display: inline-block;
        padding: 7px 12px;
        border-radius: 999px;
        background: rgba(96, 165, 250, 0.12);
        border: 1px solid rgba(96, 165, 250, 0.25);
        color: #93c5fd;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 1px;
        margin-bottom: 16px;
    }

    .hero h1 {
        color: #f8fafc;
        font-size: clamp(2rem, 4vw, 3.1rem);
        font-weight: 800;
        line-height: 1.2;
        margin: 0 0 14px 0;
    }

    .hero p {
        color: #bdcbe0;
        font-size: 1.05rem;
        line-height: 1.9;
        max-width: 720px;
        margin: 0;
    }

    /* Section headings */
    .section-title {
        display: flex;
        align-items: center;
        gap: 10px;
        color: #bfdbfe;
        font-size: 1.15rem;
        font-weight: 750;
        margin: 24px 0 16px;
    }

    /* Form container */
    [data-testid="stForm"] {
        padding: 24px;
        background: rgba(15, 23, 42, 0.82);
        border: 1px solid #263449;
        border-radius: 20px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.12);
    }

    /* Input labels */
    [data-testid="stWidgetLabel"] p {
        color: #cbd5e1;
        font-weight: 600;
        font-size: 0.91rem;
    }

    /* Input fields */
    [data-baseweb="select"] > div,
    [data-baseweb="input"] > div {
        background-color: #111c2e;
        border-color: #334155;
        border-radius: 10px;
    }

    [data-baseweb="select"] > div:hover,
    [data-baseweb="input"] > div:hover {
        border-color: #60a5fa;
    }

    /* Buttons */
    div[data-testid="stFormSubmitButton"] button,
    div.stButton > button {
        min-height: 48px;
        border-radius: 12px;
        border: 1px solid #3b82f6;
        background: linear-gradient(100deg, #2563eb, #4f46e5);
        color: white;
        font-size: 1rem;
        font-weight: 700;
        transition: all 0.2s ease;
    }

    div[data-testid="stFormSubmitButton"] button:hover,
    div.stButton > button:hover {
        border-color: #93c5fd;
        background: linear-gradient(100deg, #1d4ed8, #4338ca);
        box-shadow: 0 7px 22px rgba(37, 99, 235, 0.25);
        transform: translateY(-1px);
    }

    /* Metrics */
    [data-testid="stMetric"] {
        padding: 20px;
        background: linear-gradient(145deg, #111c2e, #0d1727);
        border: 1px solid #293950;
        border-radius: 16px;
    }

    [data-testid="stMetricLabel"] {
        color: #94a3b8;
    }

    [data-testid="stMetricValue"] {
        color: #f8fafc;
        font-weight: 800;
    }

    /* Progress bar */
    [data-testid="stProgressBar"] > div {
        background-color: #1e293b;
        border-radius: 999px;
        height: 10px;
    }

    [data-testid="stProgressBar"] > div > div {
        background: linear-gradient(90deg, #3b82f6, #818cf8);
        border-radius: 999px;
    }

    /* Expanders */
    [data-testid="stExpander"] {
        background: #0f192a;
        border: 1px solid #263449;
        border-radius: 12px;
    }

    /* Dividers */
    hr {
        border-color: #253247;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.85rem;
        line-height: 1.9;
        padding-top: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)



# ==================================================
# 3. Constants
# ==================================================
API_URL = "http://127.0.0.1:8000"
PREDICT_URL = f"{API_URL}/predict"



# ==================================================
# Footer
# ==================================================
st.markdown(
    """
    <div class="footer">
        <strong>Telco Churn AI</strong>
        <br>
        Machine Learning · FastAPI · Streamlit
        <br>
        Built as an AI Engineering Portfolio Project
        <br>
        تنبؤات النموذج احتمالية ولا تضمن السلوك الفعلي للعميل.
    </div>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# 5. Sidebar
# ==================================================
with st.sidebar:
    st.title("🧠 Telco Churn AI")
    st.caption("Machine Learning Portfolio Project")

    st.divider()

    st.markdown("### عن التطبيق")
    st.write(
        "يتوقع التطبيق احتمالية مغادرة العميل "
        "اعتماداً على بيانات الاشتراك والخدمات."
    )

    st.markdown("### التقنيات")
    st.markdown(
        "- Python\n"
        "- Scikit-learn\n"
        "- FastAPI\n"
        "- Streamlit\n"
        "- REST API"
    )

    st.divider()

    st.caption("Model: Logistic Regression")
    st.caption("Decision Threshold: 30%")


# ==================================================
# 6. Customer Input Form
# ==================================================
with st.form("customer_form"):

    st.markdown(
        '<div class="section-title">👤 البيانات الشخصية</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("الجنس | Gender", ["Female", "Male"])
        senior_citizen = st.selectbox(
            "كبير بالسن؟ | Senior Citizen",
            [0, 1],
            format_func=lambda x: "نعم" if x == 1 else "لا",
        )

    with col2:
        partner = st.selectbox("شريك | Partner", ["Yes", "No"])
        dependents = st.selectbox("معالون | Dependents", ["Yes", "No"])

    with col3:
        paperless_billing = st.selectbox(
            "الفواتير الإلكترونية | Paperless Billing",
            ["Yes", "No"],
        )

    st.divider()

    st.markdown(
        '<div class="section-title">📡 الاشتراك والخدمات</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        tenure = st.number_input(
            "مدة الاشتراك بالأشهر | Tenure",
            min_value=0,
            max_value=100,
            value=12,
        )

        contract = st.selectbox(
            "نوع العقد | Contract",
            ["Month-to-month", "One year", "Two year"],
        )

    with col2:
        phone_service = st.selectbox(
            "خدمة الهاتف | Phone Service",
            ["Yes", "No"],
        )

        multiple_lines = st.selectbox(
            "خطوط متعددة | Multiple Lines",
            ["No", "Yes", "No phone service"],
        )

    with col3:
        internet_service = st.selectbox(
            "خدمة الإنترنت | Internet Service",
            ["DSL", "Fiber optic", "No"],
        )

        payment_method = st.selectbox(
            "طريقة الدفع | Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)",
            ],
        )

    st.markdown("#### خدمات الإنترنت")

    col1, col2, col3 = st.columns(3)

    with col1:
        online_security = st.selectbox(
            "الأمان الإلكتروني | Online Security",
            ["No", "Yes", "No internet service"],
        )
        online_backup = st.selectbox(
            "النسخ الاحتياطي | Online Backup",
            ["No", "Yes", "No internet service"],
        )

    with col2:
        device_protection = st.selectbox(
            "حماية الجهاز | Device Protection",
            ["No", "Yes", "No internet service"],
        )
        tech_support = st.selectbox(
            "الدعم الفني | Tech Support",
            ["No", "Yes", "No internet service"],
        )

    with col3:
        streaming_tv = st.selectbox(
            "البث التلفزيوني | Streaming TV",
            ["No", "Yes", "No internet service"],
        )
        streaming_movies = st.selectbox(
            "بث الأفلام | Streaming Movies",
            ["No", "Yes", "No internet service"],
        )

    st.divider()

    st.markdown(
        '<div class="section-title">💳 البيانات المالية</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        monthly_charges = st.number_input(
            "الفاتورة الشهرية | Monthly Charges",
            min_value=0.0,
            max_value=200.0,
            value=70.0,
            step=0.5,
        )

    with col2:
        total_charges = st.number_input(
            "إجمالي الفواتير | Total Charges",
            min_value=0.0,
            value=840.0,
            step=10.0,
        )

    st.caption(
        "تأكد من أن إجمالي الفواتير يتوافق مع مدة الاشتراك "
        "والفاتورة الشهرية قدر الإمكان."
    )

    submitted = st.form_submit_button(
        "🔮 تحليل احتمالية مغادرة العميل",
        type="primary",
    )


# ==================================================
# 7. Send Prediction Request
# ==================================================
if submitted:

    if tenure > 0 and total_charges == 0:
        st.warning(
            "تنبيه: العميل لديه مدة اشتراك، لكن إجمالي الفواتير صفر. "
            "تأكد من صحة البيانات."
        )

    input_data = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
    }

    with st.spinner("جاري تحليل بيانات العميل..."):

        try:
            response = requests.post(
                PREDICT_URL,
                json=input_data,
                timeout=15,
            )

            if response.status_code == 200:

                result = response.json()

                if result.get("status") != "success":
                    st.error(
                        result.get("message", "حدث خطأ أثناء التنبؤ.")
                    )

                else:
                    prediction = result["prediction"]
                    probability = float(result["churn_probability"])
                    threshold = float(result["threshold"]) * 100

                    st.divider()
                    st.header("🎯 نتيجة التحليل")

                    metric1, metric2, metric3 = st.columns(3)

                    metric1.metric(
                        "احتمال المغادرة",
                        f"{probability:.2f}%",
                    )

                    metric2.metric(
                        "عتبة القرار",
                        f"{threshold:.0f}%",
                    )

                    metric3.metric(
                        "الحالة",
                        "مغادرة محتملة"
                        if "Yes" in prediction
                        else "استمرار محتمل",
                    )

                    st.progress(
                        min(max(probability / 100, 0.0), 1.0),
                        text=f"Churn Probability: {probability:.2f}%",
                    )

                    st.markdown(
                        '<div class="result-card">',
                        unsafe_allow_html=True,
                    )

                    if "Yes" in prediction:
                        st.error("⚠️ احتمال مرتفع نسبياً لمغادرة العميل")
                        st.write(
                            "يمكن استخدام هذه النتيجة لتحديد العملاء "
                            "الذين قد يستفيدون من عروض الاحتفاظ."
                        )
                    else:
                        st.success("✅ النموذج يتوقع استمرار العميل")
                        st.write(
                            "الاحتمال المقدّر أقل من عتبة القرار "
                            "المستخدمة في النموذج."
                        )

                    st.markdown("</div>", unsafe_allow_html=True)


            elif response.status_code == 422:
                st.error(
                    "البيانات المرسلة غير مطابقة لمتطلبات الـ API. "
                    "تحقق من أسماء الحقول والقيم."
                )
                st.code(response.text)

            else:
                st.error(
                    f"فشل الطلب. HTTP Status: {response.status_code}"
                )
                st.code(response.text)

        except requests.exceptions.ConnectionError:
            st.error(
                "تعذر الاتصال بـ FastAPI. "
                "تأكد من تشغيل الخادم على 127.0.0.1:8000."
            )

        except requests.exceptions.Timeout:
            st.error("استغرق الخادم وقتاً طويلاً للرد. حاول مجدداً.")

        except (ValueError, KeyError) as error:
            st.error(f"تعذر تفسير استجابة الـ API: {error}")

        except requests.exceptions.RequestException as error:
            st.error(f"حدث خطأ أثناء إرسال الطلب: {error}")



# ==================================================
# Footer
# ==================================================
st.markdown(
    """
    <div class="footer">
        <strong>Telco Churn AI</strong>
        <br>
        Machine Learning · FastAPI · Streamlit
        <br>
        Built as an AI Engineering Portfolio Project
        <br>
        تنبؤات النموذج احتمالية ولا تضمن السلوك الفعلي للعميل.
    </div>
    """,
    unsafe_allow_html=True,
)

