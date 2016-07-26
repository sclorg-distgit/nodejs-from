%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

# Disabled as BR: for tests are not in fedora
%global enable_tests 0

%global module_name from

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        0.1.3
Release:        4%{?dist}
Summary:        Easy way to make a Readable Stream

License:        MIT or ASL 2.0
URL:            http://github.com/dominictarr/from
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(asynct)
BuildRequires:  %{?scl_prefix}npm(stream-spec)
BuildRequires:  %{?scl_prefix}npm(assertions)
%endif

%description
%{summary}.

%prep
%setup -q -n package
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
asynct test/*.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.markdown LICENSE.MIT LICENSE.APACHE2
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 0.1.3-4
- Use macro to find provides and requires

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 0.1.3-3
- Enable scl macros, fix license macro for el6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.1.3-1
- Initial packaging