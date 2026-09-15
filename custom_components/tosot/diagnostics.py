"""Diagnostics support for the tosot integration."""

from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.core import HomeAssistant

from . import TosotConfigEntry

# Sensitive fields stored in the config entry — never expose them in a
# diagnostics download. ``name``/``title`` carry the TOSOT account display name
# (often the registered phone number), so they are personal data too.
TO_REDACT = frozenset(
    {
        "access_token",
        "refresh_token",
        "open_id",
        "name",
        "title",
    }
)


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant,
    entry: TosotConfigEntry,
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    return {"entry": async_redact_data(entry.as_dict(), TO_REDACT)}
