#!/usr/bin/env python3
"""Tests for the deterministic UDF profile derivation."""

import unittest

from derive_profile import derive_profile


BASE = {
    "assessment_id": "test-001",
    "criticality": "low",
    "reversibility": "easy",
    "regulated": False,
    "data_sensitivity": "public",
    "sovereignty": "none",
    "autonomy": "advisory",
    "execution_topology": "local",
    "change_cadence": "iterative",
    "organizational_maturity": "defined",
}


class DeriveProfileTests(unittest.TestCase):
    def test_low_risk_profile_remains_light(self) -> None:
        profile = derive_profile(BASE)
        self.assertEqual(profile["assurance_level"], "low")
        self.assertEqual(profile["documentation_depth"], "minimal")
        self.assertEqual(profile["human_oversight"], "advisory")

    def test_regulated_irreversible_profile_is_strict(self) -> None:
        assessment = BASE | {
            "regulated": True,
            "reversibility": "irreversible",
            "data_sensitivity": "restricted",
            "autonomy": "high",
        }
        profile = derive_profile(assessment)
        self.assertEqual(profile["assurance_level"], "critical")
        self.assertEqual(profile["documentation_depth"], "regulated")
        self.assertEqual(profile["human_oversight"], "mandatory")
        statuses = {item["id"]: item["status"] for item in profile["capabilities"]}
        self.assertEqual(statuses["audit_trail"], "required")
        self.assertEqual(statuses["execution_sandbox"], "required")

    def test_rag_and_staffing_are_contextual(self) -> None:
        assessment = BASE | {"rag_requested": True, "staffing_requested": True}
        profile = derive_profile(assessment)
        statuses = {item["id"]: item["status"] for item in profile["capabilities"]}
        self.assertEqual(statuses["rag"], "recommended")
        self.assertEqual(statuses["agent_staffing"], "recommended")

    def test_missing_required_input_fails(self) -> None:
        with self.assertRaises(ValueError):
            derive_profile({"assessment_id": "incomplete"})


if __name__ == "__main__":
    unittest.main()
