class ProjectCapabilities:
    def get_all_capabilities_by_targets(self):
        return {target: self.get_capabilities_by_target(target) for target in self.objects.get_targets()}

    def get_capabilities_by_target(self, target):
        try:
            return self._get_targets_attributes()[target.get_id()].SystemCapabilities
        except KeyError:
            return None

    def get_capabilities_by_target_name(self, name):
        target = self.get_target_by_name(name)
        return self.get_capabilities_by_target(target) if target != None else None

    def _get_targets_attributes(self):
        return self.objects.get_objects_in_section(u'PBXProject')[0].attributes.TargetAttributes