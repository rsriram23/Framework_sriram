from pages.support_page import SupportPage


class TestSupportPage:


    def test_14G_manual_download(self):
        self.sp = SupportPage()
        final_page_received=self.sp.search_14g_guide()
        final_page_expected="https://www.dell.com/support/product-details/en-in/product/cloud-for-microsoft-azure-stack14g/overview"

        assert final_page_received==final_page_expected,f"Expected to navigate to: {final_page_expected} but script navigated to: {final_page_received}."

    def test_RASR_documentation(self):
        self.sp = SupportPage()
        rasr_page_received=self.sp.search_rasr_document()
        rasr_page_expected="https://www.dell.com/support/search/en-in#q=RASR&f-langFacet=en"
        assert rasr_page_received == rasr_page_expected, f"Expected to navigate to: {rasr_page_expected} but script navigated to: {rasr_page_received}."